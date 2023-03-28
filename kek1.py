from pygame import *
okko = display.set_mode(700,400)
class igrok():
        def upr():
                self.ris()
                knopki = key.get_pressed():
                        if knopki[K_RIGHT] and self.rect.x<625:
                                self.last_pos_x = self.rect.x
                                self.rect.x += razmer_jizi
                                direct = 'r'
                        if knopki[K_LEFT] and self.rect.x>0:
                                self.last_pos_x = self.rect.x
                                self.rect.x -= razmer_jizi
                                direct = 'l'
                        if knopki[K_UP] and self.rect.y>0:
                                self.last_pos_y = self.rect.y
                                self.rect.y -= razmer_jizi
                                direct = 't'
                        if knopki[K_DOWN] and self.rect.y<340:
                                self.last_pos_y = self.rect.y
                                self.rect.y += razmer_jizi
                                direct = 'd'
