 lives_label = main_font.render(f"Lives:{lives}" ,1, (255,255,255))
        level_label = main_font.render(f"Level:{level}",1,(255,255,255))
        WIN.blit(lives_label,(10,10))
        WIN.blit(level_label,(WIDTH-level_label.get_width()-10,10))