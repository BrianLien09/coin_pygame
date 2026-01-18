import pygame
import random
import asyncio

# --- 遊戲設定 ---
WIDTH, HEIGHT = 800, 600
FPS = 60
WINNING_SCORE = 500  # 勝利條件

# 顏色定義
COLORS = {
    "bg": (20, 20, 35),
    "player": (0, 255, 255),
    "enemy": (255, 80, 80),
    "bullet": (255, 255, 100),
    "particle": (255, 150, 50),
    "white": (255, 255, 255)
}

# --- 1. 粒子系統 (具備透明度變化) ---
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        size = random.randint(2, 5)
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.color = list(COLORS["particle"])
        self.alpha = 255
        self.image.fill((*self.color, self.alpha))
        self.rect = self.image.get_rect(center=(x, y))
        self.vel_x = random.uniform(-4, 4)
        self.vel_y = random.uniform(-4, 4)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.alpha -= 10  # 每一幀減少透明度
        if self.alpha <= 0:
            self.kill()
        else:
            self.image.fill((*self.color, self.alpha))

# --- 2. 子彈類別 ---
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 15))
        self.image.fill(COLORS["bullet"])
        self.rect = self.image.get_rect(centerx=x, bottom=y)
        self.speed = -12

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

# --- 3. 敵人類別 (具備隨機旋轉動畫) ---
class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.size = random.randint(30, 50)
        self.original_image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.rect(self.original_image, COLORS["enemy"], (0, 0, self.size, self.size), border_radius=8)
        
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(x=random.randint(0, WIDTH - self.size), y=-self.size)
        self.speed = speed
        self.angle = 0
        self.rot_speed = random.randint(-5, 5) # 隨機旋轉速度

    def update(self):
        # 旋轉邏輯
        self.angle = (self.angle + self.rot_speed) % 360
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)
        
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

# --- 4. 玩家類別 (具備自動連發) ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, COLORS["player"], [(25, 0), (0, 40), (50, 40)])
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 20))
        self.hp = 3
        self.shoot_delay = 200
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0:
            self.rect.x -= 10
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < WIDTH:
            self.rect.x += 10

# --- 5. 遊戲主控制器 ---
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("TUF Gaming - 終極射擊戰 ")
        self.clock = pygame.time.Clock()
        self.font_title = pygame.font.SysFont("Arial", 64, bold=True)
        self.font_ui = pygame.font.SysFont("Arial", 28, bold=True)
        
        self.state = "MENU"
        self.reset_game()

    def reset_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.particles = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.score = 0
        self.spawn_timer = 0

    def draw_button(self, text, y_offset, color, hover_color, callback):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        btn_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + y_offset, 200, 60)
        
        current_color = hover_color if btn_rect.collidepoint(mouse) else color
        pygame.draw.rect(self.screen, current_color, btn_rect, border_radius=12)
        
        txt_surf = self.font_ui.render(text, True, COLORS["white"])
        txt_rect = txt_surf.get_rect(center=btn_rect.center)
        self.screen.blit(txt_surf, txt_rect)
        
        if btn_rect.collidepoint(mouse) and click[0] == 1:
            pygame.time.delay(150)
            callback()

    async def run(self):
        while True:
            self.screen.fill(COLORS["bg"])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            if self.state == "MENU":
                title = self.font_title.render("SPACE DEFENDER", True, COLORS["player"])
                self.screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//3)))
                self.draw_button("START", 50, (0, 150, 0), (0, 200, 0), lambda: setattr(self, 'state', 'PLAYING'))

            elif self.state == "PLAYING":
                # 自動連發偵測 (按住空格)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    now = pygame.time.get_ticks()
                    if now - self.player.last_shot > self.player.shoot_delay:
                        b = Bullet(self.player.rect.centerx, self.player.rect.top)
                        self.all_sprites.add(b)
                        self.bullets.add(b)
                        self.player.last_shot = now

                # 敵人生成
                self.spawn_timer += 1
                if self.spawn_timer > 25:
                    e = Enemy(random.randint(4, 8))
                    self.all_sprites.add(e)
                    self.enemies.add(e)
                    self.spawn_timer = 0

                # 更新物件
                self.all_sprites.update()
                self.particles.update()

                # 碰撞判定：子彈 vs 敵人
                hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
                for hit in hits:
                    self.score += 20
                    for _ in range(10): # 產生透明粒子碎裂效果
                        self.particles.add(Particle(hit.rect.centerx, hit.rect.centery))

                # 碰撞判定：玩家 vs 敵人
                if pygame.sprite.spritecollide(self.player, self.enemies, True):
                    self.player.hp -= 1
                    if self.player.hp <= 0:
                        self.state = "GAMEOVER"

                # 勝利判定
                if self.score >= WINNING_SCORE:
                    self.state = "WIN"

                # 繪製
                self.all_sprites.draw(self.screen)
                self.particles.draw(self.screen)
                
                # UI
                score_txt = self.font_ui.render(f"SCORE: {self.score} / {WINNING_SCORE}", True, COLORS["white"])
                hp_txt = self.font_ui.render(f"HP: {self.player.hp}", True, COLORS["enemy"])
                self.screen.blit(score_txt, (20, 20))
                self.screen.blit(hp_txt, (20, 55))

            elif self.state == "GAMEOVER":
                over_txt = self.font_title.render("GAME OVER", True, COLORS["enemy"])
                self.screen.blit(over_txt, over_txt.get_rect(center=(WIDTH//2, HEIGHT//3)))
                self.draw_button("RETRY", 50, (150, 0, 0), (200, 0, 0), self.reset_game)

            elif self.state == "WIN":
                win_txt = self.font_title.render("VICTORY!", True, (0, 255, 100))
                self.screen.blit(win_txt, win_txt.get_rect(center=(WIDTH//2, HEIGHT//3)))
                self.draw_button("PLAY AGAIN", 50, (0, 100, 200), (0, 150, 255), self.reset_game)

            pygame.display.flip()
            self.clock.tick(FPS)
            await asyncio.sleep(0)

if __name__ == "__main__":
    game = Game()
    asyncio.run(game.run())