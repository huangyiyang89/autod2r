from autod2r import *
import logging

d2r = autod2r()
d2r.set_foreground()
while True:
    try:

        if not d2r.is_map_open():
            d2r.key_press(VK_TAB)
            time.sleep(0.5)

        d2r.cast(VK_W, PLAYER_X, PLAYER_Y)
        time.sleep(0.7)

        while d2r.move_to_ref_location("ref_hjls.png", -20, 164):
            time.sleep(1)

        while d2r.move_to_ref_location("ref_hjls.png", -89, 175):
            time.sleep(1)

        d2r.click_door("ref_hjls.png", -113, 155)

        d2r.wait_for_loading()
        time.sleep(1)
        d2r.left_click(1163, 112)  # 走一步开地图
        time.sleep(1)

        while d2r.move_to_ref_location("ref_nlskdsd_new.png", 128, -4):
            time.sleep(1)

        for i in range(30):
            d2r.cast(VK_Q, PLAYER_X+random.randint(-500, 500),
                     PLAYER_Y+random.randint(-300, 300))
            time.sleep(0.1)
        time.sleep(0.5)
        while d2r.move_to_ref_location("ref_nlskdsd_new.png", 200, -42):
            time.sleep(1)
            d2r.use_drug_if_hp_is_low()
        while d2r.move_to_ref_location("ref_nlskdsd_new.png", 230, -68):
            time.sleep(1)
            d2r.use_drug_if_hp_is_low()

        x, y = 1320, 344
        d2r.cast(VK_W, x, y)
        time.sleep(1)
        for i in range(2):
            d2r.cast(VK_S, x, y)
            time.sleep(0.7)
            d2r.cast(VK_R, x, y)
            time.sleep(0.7)
            d2r.use_drug_if_hp_is_low()
            d2r.cast(VK_Z, x, y)
            time.sleep(0.7)
            d2r.cast(VK_D, x, y)
            time.sleep(0.7)
            d2r.use_drug_if_hp_is_low()
            d2r.cast(VK_Z, x, y)
            time.sleep(0.7)
            d2r.cast(VK_E, x, y)
            time.sleep(0.1)
            d2r.cast(VK_Z, x, y)
            time.sleep(0.7)
            d2r.use_drug_if_hp_is_low()
        d2r.cast(VK_E, x, y)
        time.sleep(0.7)
        d2r.cast(VK_E, x, y)
        time.sleep(0.7)
        d2r.use_drug_if_hp_is_low()
        d2r.cast(VK_E, x, y)
        time.sleep(0.7)
        d2r.cast(VK_E, x, y)
        time.sleep(0.7)

        for i in range(5):
            x, y = d2r.find_drops()
            if x < 0 and y < 0:
                break
            time.sleep(1)

    except Exception as e:
        logging.exception(e)

    d2r.restart_game()

    # drugs=d2r.get_drugs()
