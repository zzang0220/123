import pygame
import random
import time
import sys

# 초기화
pygame.init()
screen_width = 530
screen_height = 820
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 이름
pygame.display.set_caption("똥피하기")

# 배경음악
pygame.mixer.music.load("C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/music/Game 1.mp3")
pygame.mixer.music.play(-1)

# 시계
clock = pygame.time.Clock()

# 스테이지 정보
stages = {
    1: {"background": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/st1z.png", "background_music": "pygame/music/Game 1.mp3", "character_speed": 0.3, "enemy_speed": 20, "army_speed": 10,
        "score_limit": 4, "enemy_image": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/ddongg.png", "army_image": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/army1.png"},
    2: {"background": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/st2z.png", "background_music": "pygame/music/Game 2.mp3", "character_speed": 0.3, "enemy_speed": 20, "army_speed": 10,
        "score_limit": 8, "enemy_image": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/ddongg.png", "army_image": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/army2.png"},
    3: {"background": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/st3z.png", "background_music": "pygame/music/Game 3.mp3", "character_speed": 0.3, "enemy_speed": 20, "army_speed": 10,
        "score_limit": 12, "enemy_image": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/ddongg.png", "army_image": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/army3.png"},
    4: {"background": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/st4z.png", "background_music": "pygame/music/Game 4.mp3", "character_speed": 0.3, "enemy_speed": 20, "army_speed": 10,
        "score_limit": 16, "enemy_image": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/ddongg.png", "army_image": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/army4.png"},
    5: {"background": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/st5z.png", "background_music": "pygame/music/Game 5.mp3", "character_speed": 0.3, "enemy_speed": 20, "army_speed": 10,
        "score_limit": 20, "enemy_image": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/ddongg.png", "army_image": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/army5.png"},
    6: {"background": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/stFz.png", "background_music": "pygame/music/Game 6.mp3", "character_speed": 0.3, "enemy_speed": 20, "army_speed": 10,
        "score_limit": 24, "enemy_image": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/ddongg.png", "army_image": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/army6.png"},
    7: {"background": "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/end_background.png", "background_music": "pygame/music/Game 1.mp3", "character_speed": 0.3, "enemy_speed": 0, "army_speed": 0,
        "score_limit": 100, "enemy_image": None, "army_image": None}
}

# 현재 스테이지
current_stage = 1

# 초기 스테이지 로딩
def load_stage(stage_number):
    global background, enemy_speed, character_speed, army_speed, background_music
    stage_data = stages[stage_number]
    background = pygame.image.load(stage_data["background"])
    enemy_speed = stage_data["enemy_speed"]
    character_speed = stage_data["character_speed"]
    army_speed = stage_data["army_speed"]
    background_music = stage_data["background_music"]

load_stage(current_stage)
pygame.mixer.music.load(background_music)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# 초기 Army 이미지 설정
army_image = stages[current_stage]["army_image"]
army = pygame.image.load(army_image)
army_size = army.get_rect().size
army_width = army_size[0]
army_height = army_size[1]
army_x_pos = random.randint(0, screen_width - army_width)
army_y_pos = 0

# 게임 시작 여부
game_started = False

# 배경 이미지
background_image = pygame.image.load("C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/start_screen_background.png")

# 스타트 버튼 이미지
start_button_image = pygame.image.load("C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/start_button.png")
start_button_rect = start_button_image.get_rect()
start_button_rect.center = (screen_width // 2, screen_height // 2)

# 게임 오버 여부
game_over = False

# 게임 오버 음악
game_over_music = pygame.mixer.Sound("C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/music/losing.wav")

# 캐릭터
character = pygame.image.load("C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/man2.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height
to_x = 0

# 똥
enemy = pygame.image.load(stages[current_stage]["enemy_image"])
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0

# 특수 아이템 관련 설정
special_items = []  # 특수 아이템을 저장하는 리스트
special_item_images = [
    "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/ice.png",
    "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/lightning.png",
    "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/item3.png"
]

# 특수 아이템 떨어지는 간격 (프레임 수)
special_item_spawn_interval = 150

# 특수 아이템 이미지 불러오기 함수
def load_special_item():
    if current_stage != 7:  # Prevent special items in Stage 7
        special_item_image_path = random.choice(special_item_images)
        special_item_image = pygame.image.load(special_item_image_path)
        special_item_size = special_item_image.get_rect().size
        special_item_width = special_item_size[0]
        special_item_height = special_item_size[1]
        special_item_x_pos = random.randint(0, screen_width - special_item_width)
        special_item_y_pos = 0
        special_item = {
            "image": special_item_image,
            "x": special_item_x_pos,
            "y": special_item_y_pos,
            "path": special_item_image_path
        }
        special_items.append(special_item)

# 특수 아이템 효과 적용 함수
def apply_special_item_effect(special_item_path):
    global character_speed, enemy_speed, score, special_item_effect_active, special_item_effect_start_time, special_item_effect_duration

    if special_item_path == "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/ice.png":
        # 캐릭터 속도 두 배 증가
        character_speed *= 2
    elif special_item_path == "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/lightning.png":
        # 적 속도 절반 감소
        enemy_speed /= 2
    elif special_item_path == "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/item3.png":
        # 점수 3점 증가
        score += 3

    special_item_effect_active = True
    special_item_effect_start_time = time.time()
    special_item_effect_duration = 10  # 효과 지속 시간 (초)

# 다음 스테이지로 넘어가는 함수
def next_stage():
    global current_stage, game_started, game_over, background_music, army_image, army
    current_stage += 1
    if current_stage in stages:
        load_stage(current_stage)
        pygame.mixer.music.load(background_music)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        if current_stage != 7:
            army_image = stages[current_stage]["army_image"]
            army = pygame.image.load(army_image)
            army_size = army.get_rect().size
            army_width = army_size[0]
            army_height = army_size[1]
            army_x_pos = random.randint(0, screen_width - army_width)
        
        # 게임 시작 여부를 True로 설정
        game_started = True
    else:
        game_over = True

# 다음 스테이지 버튼 이미지
next_stage_button_image = pygame.image.load("C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/next_stage_button.png")
next_stage_button_rect = next_stage_button_image.get_rect()
next_stage_button_rect.center = (screen_width // 2, screen_height // 2)

# 다음 스테이지 화면 배경 이미지
next_stage_bg_image = pygame.image.load("C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/next_stage_bg.png")



# 스토리 이미지 파일 경로
story_images = [
    "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/story1.png",
    "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/story2.png",
    "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/story3.png",
    "C:/Users/82109/OneDrive/바탕 화면/Python1/repos_python/pygame/image/story4.png"
]
current_story_image_index = 0
story_image = pygame.image.load(story_images[current_story_image_index])
story_image_rect = story_image.get_rect()
story_image_rect.center = (screen_width // 2, screen_height // 2)

show_story = True  # 스토리 보여주기 여부

while show_story:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                current_story_image_index += 1
                if current_story_image_index < len(story_images):
                    story_image = pygame.image.load(story_images[current_story_image_index])
                else:
                    show_story = False

    screen.blit(story_image, story_image_rect)
    pygame.display.update()
    clock.tick(60)

# 스토리 종료 후 게임 시작 준비
current_story_image_index = 0  # 스토리 이미지 인덱스 초기화
show_story = False





# 게임 루프
special_item_spawn_timer = 0
score = 0
special_item_effect_active = False
special_item_effect_start_time = None
special_item_effect_duration = 10  # 효과 지속 시간 (초)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if not game_started:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    game_started = True
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= character_speed
                elif event.key == pygame.K_RIGHT:
                    to_x += character_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0

    if game_started:
        # 게임 로직 부분
        dt = clock.tick(30)
        character_x_pos += to_x * dt
        if current_stage != 7:
            enemy_y_pos += enemy_speed
            army_y_pos += army_speed

        if enemy_y_pos > screen_height:
            enemy_y_pos = 0
            enemy_x_pos = random.randint(0, screen_width - enemy_width)

        if army_y_pos > screen_height:
            army_y_pos = 0
            army_x_pos = random.randint(0, screen_width - army_width)

        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        enemy_rect = enemy.get_rect()
        enemy_rect.left = enemy_x_pos
        enemy_rect.top = enemy_y_pos

        army_rect = army.get_rect()
        army_rect.left = army_x_pos
        army_rect.top = army_y_pos

        if character_rect.colliderect(enemy_rect):
            game_over = True

        if character_rect.colliderect(army_rect):
            score += 1
            army_y_pos = 0
            army_x_pos = random.randint(0, screen_width - army_width)

            if score > stages[current_stage]["score_limit"]:
                game_started = False
                screen.blit(next_stage_bg_image, (0, 0))
                screen.blit(next_stage_button_image, next_stage_button_rect)
                pygame.display.update()

                next_stage_button_clicked = False
                while not next_stage_button_clicked:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game_over = True
                            next_stage_button_clicked = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if next_stage_button_rect.collidepoint(event.pos):
                                next_stage()
                                next_stage_button_clicked = True

        if current_stage != 7:  # Special items do not appear in Stage 7
            special_item_spawn_timer += 1
            if special_item_spawn_timer >= special_item_spawn_interval:
                load_special_item()
                special_item_spawn_timer = 0

            for special_item in special_items[:]:
                special_item["y"] += 5
                special_item_rect = special_item["image"].get_rect()
                special_item_rect.left = special_item["x"]
                special_item_rect.top = special_item["y"]

                if special_item_rect.colliderect(character_rect):
                    apply_special_item_effect(special_item["path"])
                    special_items.remove(special_item)

                if special_item["y"] > screen_height:
                    special_items.remove(special_item)

        current_time = time.time()
        if special_item_effect_active and current_time - special_item_effect_start_time > special_item_effect_duration:
            character_speed /= 2
            enemy_speed *= 2
            special_item_effect_active = False
            special_item_effect_start_time = None
            special_item_effect_duration = 10

        screen.blit(background, (0, 0))
        screen.blit(character, (character_x_pos, character_y_pos))
        if current_stage != 7:
            screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
            screen.blit(army, (army_x_pos, army_y_pos))

        for special_item in special_items:
            screen.blit(special_item["image"], (special_item["x"], special_item["y"]))

        game_font = pygame.font.Font(None, 40)
        score_display = game_font.render('Score: ' + str(score), True, (255, 255, 255))
        screen.blit(score_display, (10, 10))

        pygame.display.update()
    else:
        screen.blit(background_image, (0, 0))
        screen.blit(start_button_image, start_button_rect)
        pygame.display.update()

pygame.mixer.music.stop()
game_over_music.play()
game_over_font = pygame.font.Font(None, 80)
game_over_text = game_over_font.render('Game Over', True, (255, 255, 255))
screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
pygame.display.update()
pygame.time.delay(2000)
pygame.quit()

