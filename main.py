def on_game_finished(gameName):
    global initGame, pesadilla
    initGame = False
    pesadilla = False
    sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
    sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
    sprites.destroy_all_sprites_of_kind(SpriteKind.text)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    tiles.set_current_tilemap(tilemap("""
        empty
        """))
    scroller.scroll_background_with_speed(0, 0)
    scroller.set_background_scroll_offset(0, 0)
    info.set_life(None)
    effects.confetti.end_screen_effect()
    effects.star_field.end_screen_effect()
multigame.on_game_finished(on_game_finished)

def on_life_zero():
    global initGame
    initGame = False
    game.set_game_over_message(False, "No lo conseguiste")
    game.game_over(False)
    game.set_game_over_effect(False, effects.dissolve)
multigame.on_life_zero("game", on_life_zero)

def IrFaseMulti(currentFase: str, newFase: str):
    global fase
    fase = newFase
    multigame.finish_game(currentFase)
    multigame.start_game(fase)

def on_on_start():
    pass
multigame.on_start("ending", on_on_start)

def on_on_start2():
    global reyStoryImg, princesaStoryImg, encantaStorySprite, reyStorySprite
    scene.set_background_image(img("""
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbdddbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcccfccccceeccbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbffccccccccceecceebdbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbfcccccccccccccceeeeeeeecccdddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbfccccccccccccccccccceeeeeecceebbddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcfccccccccccccccccccccccceeccceeefcdddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcfcccccccccccccccccccccccceeeccceeeeccddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbffccccccccccccccccccccccccceeeecceeeeeeebddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbffccccccccccccccccccccccccccceeeecccceeeeeeebddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbfffccccccccccccccccccccccccceeeeeeeeccccceeeeeeefbddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbcfccccccccccccccccccccccccccceebeeeeeccccfeeeeeeeeebdddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcfcccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeebdddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcccccccccccccccccccccccccccccccceeeeebeebeebbeeeeeeeeeeeeebddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcccccccccccccccccccccccccccccccccceeeeeeeeeebeeeeeebbeebeeeeebddddddddddddddddddddddddddddddddddddddddd
        bbbbbbbddddbbddbbbbdddddddddddddddddddddddddddddddddddbffcccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeebddddddddddddddddddddddddddddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbdddbddbdddddddddddddddddddddddddbfcccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeebdddddddddddddddddddddddddddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddbbbcfcccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeebddddddddddddddddddddddddddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcfcccccccccccccccccccccccccccccccccccccccceeeccceeeeeeeeeeeeeeeeeeeeeeeeeeeebddddddddddddddddddddbdddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbcccccccccccccccccccccccccccccccccccccccccceeecceeeceeeeeeeeeeeeeeeeeeeeeeeeeeebbdbbdddddbbbbbbbbdbdddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbfffccccccccccfcccccccccccccccccccccccccccccccceecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbdbbbbbbbbbbbbbbbbbbbbbbbdddbdd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcfcccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbdbbbbbbbbbbbbbbbbddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeccceeeeeeeeeeeeeeeeeeeeeeeeeeccbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbcbcbbccbbbccccccffccccccccccccccccccccccccfcccccccccccccccccccccccceeeeeeeeeeecceeeeeeeceeeeeeeeeeeeeeeeeeeeeeebbbbbbbccccccccccbcccbbbbc
        bbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccceeccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbccbcccb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccccccccecceeccceeeeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbbcccc
        cbccccccccbcbbbbcccccbbbbbbbcccfffcccccccccccccccccccccccccccccccccccffcccccccccccccccccceeeceeeeeeccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccbbbbbccc
        cccccbbbbbbbbbbcbcccccccffcfccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccceeeeceeeeeeceeeeeeeeeeeeeeeeeeeeeeeeecccceeeeeeeeeeeeccbbbccccccccccccc
        cbccccbbbbbbcbbcccccccccccccccccccccccccccffccfcfcccccccccccfffccccccccccccccccccccccccccceeeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccebeeeeeeeeeeeeeccccccccccccccc
        cccccbcccccccffcfffcccccccccccccccccccccccccccfcccccccccccccccccccccccccccccccccccccccecccceeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecceeeeeeeeeeeeeeccccccccccc
        ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccceeccccccccccccccceeccccceeeeeeeeeeeeeeeeeeeceeeeeeeeeccccceeeeeeccceeeeeeeeeeeeeecccccbcccc
        ccccccccccccccccccccccccccccccccccccccccccfcccfcccfffffcccccccccccccceeeeeecccceecccfcceecfcccceeeeeeeeeeeeeeeeccceeeeeccccccceeeeeeeecceeeeeeeeeeeeeeeecccccccc
        cccccccccccccccccccccccccccfcccfcccccccccccccfffcccccccccccccccccccccceebeebeecccccccfceeeecccceecccceeeeceeeeeeceeeeeeeeccccceeeeeeeeeceeeeeeeeeeeeeeeeeeeeeecc
        ccccccccccccccccccccccccccccfffccccccfffcccccccccccccccccfccccccccccccbbbebbebeeccccccceeeeeccceefcccceecceeeecceeeeeeccceeecceecceeeeeceeeeeeeeeeeeeeeeeeeeeeee
        cccccccccccccccccccccccccccccccccfcccfcccccffcccccccccccccccccccccccccceebbeebbeeeeeeeeeeeeeeceeecccccccccceeeeeeeeeccccceeecceeccfcceeeeeecceeeeeeeeeeeeeeeeeee
        cccccccccccccccccccccccccccccccccccccccfffffffcccfccccccccccffcccccccceeebbeebbeeebeeeeeeeeeeeeeeeeccccccccccecceeeeeccccceeecceeeeeeeeeeeeeeeeeeceeeeeeeeeeeeee
        ffccfffccccccccccfccccccfcccccfccffccffffccccfcccccffcccfcfcccffcccccceeeccceebeeebeeeeeeeeeeeeeebeeecceeecccccccceeeecccceeeeeeeeeebeeceeeeeeeecceeeeeeeeceeeee
        ccccccccccfffcccccccccccccfccccffffccccccccccccccccccccccfcccffffccccceecccceeeeeeebefeeeeeeeeeeeeeeeeeeecccccccceeeececeeeeeeeeefeeeeecceeeeeeeeceeeeeeeeeeeeee
        ccccccccffcccccccccccccccfccccfffccccccccccccfccccccfcccfcccfccccccccceecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecffccccceeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeeebeeeeeeeee
        ccccccccfcccccccccccccccccfffffcccccfccfffffcccccccccccfcccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        ccccffccccccccccccccfffcccccccccfccccfffffccccccccfccfffccccffcccccccccccccceebeeeeeeeeeebeeeeeeeeeeeeeeeecceeeccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        ccccccccccffccccccccfffccffffccccccfffcffccccfcccfcffccffcfffcccccccccccfffcceeeeceeeeeeeeebbeeeeeeeeeeeeeceeeeeceeeeeeebeeeeeeeeeeeeeeeeeeeeeeeceeeeeeeeeeeeeee
        cffcccfcffccccccccccccccffcffcfffffffccfffcffccccccccccfffcccfcccccccccccccccceeeeeccceeeeeeeeeeeeccceeeeceeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeeeccccccccceeeeeeeee
        cccccfffffcccccffccccfcfffffffffffffcccffcffccccccffffffcccccccccccccceecccccceeeeeecceeeeeeeeeeeccfccceeeeeeeeeeefeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccceeeeeeee
        ccccccfffcccccfcccccccccccfcffccccccccccccfccccccfcffcccfffcccccccccccceeccccccceeeecceeeeeeeeeeeecfcccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccceeeeecc
        fccccccccffccfccfcffffffccccffcccfccccccffcfcccffcfcfccfffcccccccccccccceecccccccceeeeeceeeeeeeeeeeccccccceeeeeeeeeeeeeeeeeeeeeeeeeeecceeeeeeeeceeeceecccceeeece
        cccccffccfccfffffffccfccccccccccccffcfccfcfccffffcffcccccfccccccccccccccccceccccccceeeeeeeeeeeeeeeeeeeecccceeeeeeeeeeeeeeeeeeeeeeeeeeeccceeeeeeeeeeeeeccceeeeeee
        ffccfffffffffffffffccfccccccccfcccccfcfffffcccffffcccfccffccccccccfccccccccceeccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccceeeeeeeeeeeccfceeeeee
        fffffffffffffffffffffffcccffccffffcccfcccccccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeebccceeeeeeeeeeeeeeeeeeeeeeeeecccceeeeeeeeecccceeeeee
        ccfffffffffffffffffffffccfffffffffffffccccccccccccccfccccccccccccccccccccccccccccccccccccccccccceccecceeeeccccccccceeeeecceeeeeeeceeeeeeeecccceeeeeeeecccccecccc
        ffffffffffffffffffffcffffffffcffffcffcccccccfcccffffffccccccccccccccccccccccccccccffcfffcccccfcccfcccccccefccccccccccccccccecceeeccceeeceeeccccceeeeeccccccccccc
        ffffffffffffffffffffffffffffffffffffcfffffffcccffffcccccfccffffccccfffccfffccffcccccccccccccccccccccccccceeccccfcccccccccccccceeeeffcccceecccccccccccccceccecccc
        fffffffffffffcfcfffffffffffffcffffffffcffccfcfffffcccccfffccccfcfffffcccffccfccccffcccccfccccccccccccfffcccceeccccccccffcfcccccceeccccccccfffcffcccccccceeeecccc
        fffffffffffffffcffffffffcfccffffffcffccffccccfcfcffffccccfccfccfffcffcccfccfcccccfccfccfffcccccccccccfffffceefcccccccffffccccfccceeccfffcccccccccccccccceeeeeecf
        ffffcffffccfffffffffffcfcccffffffffffffccccffffcccffceecfccfffffcccfcccccceccccccccccccccfffcffccccccffffceeeccccccccffccecccffccceeecffccccccccccccccceeeeeeccc
        ccffcccffffffffffffffccffcffccffffffcfccccfffcffccccceecccccccfccccffffcfccccfccccccccccccfffffcccfcccffffccccffffffcfccccccffffccceeccfcccffcfccccccceeeeeeccfc
        fcfccccffffffffffffffffcfffcfffffffccfcccfffccccccccceeeeeccccfccfffffffffcffffccecffceeeeccfcceecccfffcfffffffffffffffffccfffffffcccfcffcfffffcccceeefeeeeeeecf
        fcceeecfffffffffffffffffffffffffffccccccfccccecccccceeeeeeeeeffcffffffffffcfffffeeeecceeeeeeeceeeccccffcccfffffffffcffffcfcfffcfffffffffffffffffffceecceeeeeeeee
        ccceeeecccccccccfcfcffffccccffffcfcccfffffcceeeccccceeeeeeeeeeccfffffffcfcfffccfeeeeeceeeeeeeeeecffccffcffcffffffffcccffffccfcccfffffffccfffffffccfeefffceeeeeee
        fffeeeeeeeccccccccccfffcffcffcfffcfffceeefccffcccccceeeeeeeeeeecfffffccfffffffcceeeeeeecceeeeeeeecfffffffffffffffffffffffccfffcccccfffffffffffccccfcecfffcccceee
        cffeeeeeeeeefcfffffccfcccfcffcfcffccceeeeeeeeffffffffcccfeeeeeeccffccccecccccffcccceeeeccccceeeefecffffccfffffffcccffccffccfffffccccccffffffffcfcfffccfffccfccee
        eeeeeeeeeeeeecffffffccccccccccceccceeeeeeeeeeeeefccffccccfceeeeccceeeeeeeecccccccfceeefccffffccffeccffffffffffffccfffccfcccccffffcccfccffffcccfffffffccffccffccc
        eeeeeefeeeeeecfccccceeeeccccccceeeeeeecceceeeeeeccfffffcccccccccccceeccceecccccccfccecffffffffffcfcfcfccffcccccccccccccfcfccccffffffffffffcccefffffffffffffffccc
        eeeecffffffffffcccccfcfffccccfccceeeeefffffffffffffffffffffffffffffccfffeefcccfffffccccfffffccfffffcccecfcccccccccccffcffccffffcfffffffffffcfcffffffffffffffffcc
        eeeeffcfccffffffcfffffffffffcccffeeeeefffffffcffffccfffffffffffffccffffceefcffffffffffffffffcccffffcceeeccccccccccffffffffffffccfccffffffffffcffffffffffffffffcf
        eeeeccfeecffffffccffffffffffffccfeeeeecffffffffcfccffffffcffffffccccfccceeccccffcccffffffcffcccfccfccccccccccccccccfccfccfccfffcceefffffffffffffffffffffffffffcf
        eeeecffeeffffcffffffffffffffffccfffcecfffffffcccffffffffffffffffffccfccccccccccfccccffffffffffffffffffffffcccccccccfccceeeeccffffcecffffffffffffccccccccfffffffc
        eeeeffeeeffffffffffffffffffffccfffffffffffffffffffffffffffffffffffffcccffcccfccfccccfcfffffffffffffffffffffffccccfffcccfcffcffffffccccffffffffffccceeeeeefffffcc
        ceefffcecfffffffffffffffffffffffffffffffffffffffffffffffccfccfffffffffffffffffccfcfffffffffffffffffffffffffffffffffffffffffffffffcffccfffffffffffffcceeeeecfcfcc
        fffffffccccffffffffffffffffffffffffffffffffffffffffffffccccccccccccffffffffffffffffcffffffffffffffffffcfffcffffffffffffffffffffffcfffcccfffffffffffffffceececfcf
        ffffffffffccffffffffcccccfffffffffffffffffffffccccccccfcccccccccffffffffffffffffffffffffffffffffffffcfcfcccfffffffffffffffffffffffffffffffffffffffccfffccfeffccf
        fffffffffffffcccccccccccfffffffffffffffffffccccccccccccccccccccccfffffffffffffffffffcffffffffffffffffccccccfffffffffffffffffffffffffffffffffffffffcecffceeefcfff
        ffffffffffffcccccccccccccccccfffffffffccffcccccccccccccccccccccccccfffffffffffffffffcfffffffffffffffcffcccfffffffffffffffffffffffffffffffffffffffffeeeeeeeeeeeff
        ccccccccccccccccecccccccbccccfffccccffcccccccccccccccccccccccccccccfffffffffffffffffffffffffffffffffccfffffffffffffffffffffcffffffffffffffffffffffceeeeeeeeeeecf
        cccccccccccccccceeccccccccccccccccccffccbbccccccccccccccccccccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffccecfeeeeeeeff
        ccccccccccccccfceeeccccccccccccccccccfcccccccccccccccccccccccccccffffffffffffffffffffffffffffffffffffffffffffccffffffffffffffcffffffffffffffffffffffcccfeeeeefff
        cccccccccccccfcfceccccccccccccccccccccccccccccccccecccccccccccccccccfffffffffffffffffffffffffcfffffffffcffffccccccccccccfffffffffffffffffccfcfffffffffffceefffff
        cccccccccccfccffccfcccccccccccccccccccccccccceeeccecccccccccccccccccccccccccccccccccccccccccccccccccffccfffccccccccccccccccfccccccfffffccccccffffffffffffcffcffc
        cccccccccccffcfffffcccccccccccccccccccbbbcccceeeeeeeccccccccccccccccccccccccccccccccccccccccccccccccccccccccfcccccccccccccccccccccccccfcfffcffffffffffffffffffcf
        cccccccccccccfcccccccccccccccccccccccccbbcccceeeeeeeccceccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccffffffffffffffffffffffff
        ccccccccccccfffcccccccccccccccccccccccccccccceeeeeeeccceeeecccccccccccccccccccccccccccccccccccccccecccccccccccccccccccccccccccccccccccccfffffccfffffffffffffffff
        ccccccccccccccccccccccccccccccccccccccccccccceeeeeecccfeeeeeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccfffccccccccccccccccccccffffffffffcff
        cccccccccccccccccccccccccccccccccccccccccccceeeeeeeccffceeeeeebbbbbbbbcccccccccccccccccccccccceccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccffeeccccfeeeeeebbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbecccccccebbbccccccbcccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccbcccfffceecffceeeeeeccebbbbbbbbbbbbbbbbbbbbbcccccccebeecbeeeeebbbbbbbcccbbbbbbcccccccccccccccccccbbbccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccffffffeefffcffeeeeccbbbbbccccbbbbeebbeeebcccccccccccccceeebbeebbbbbbbebbbbebbbccccccccccccccbbbbbbbbbbbbbbbbccbbbbc
        cccccccccccccccccccccccccccccccccccccccbbbbccfffffceecfffffceeeccbbcbbbbcccceeeeeeeeeccccbcceeecccccceeeeeeeeecebbebbbbbbbeccbccccccccccbbbbbbbbbbbbbbbbbebbcccc
        cccccccccccccccfcccccccccccccccccccccccccccccfffffcffffffffffffccccccccccccccceeecffeeccebeeebeeeccccceebeeccccceeeeebbbbbbbbbbbbbbbbcccceeeebbeebbebbbbbccccccc
        cccccccccccccccfcccccccccccccccccccccccccccccffffffffffffffffcfffcccccccccccccffffffeecceeeebbbbeeeccceeeeeccccbeeeeeeebbbbcbbbbbbbbbbbbeebeeeeeeeeebebccbbbcccc
        cccccccccccccccfccccccccccccccccccccccccccccffffffffffffffffffffcccccbbcccccccffffffcfffeeeeebbbeeeecceeeeccccceeeeeeeebbbeecceeeeebbbecbbbbbbeeeeeeeeebbbebeeee
        cccccffccccecccccccccccccccccccccccccccccccffffffffffffffffffffccccccccccccfccffffffcffffceeeeeceeeeeeeeeccccceeeeeeeeeeeeeebbeeeeeebeeeeeeeeeeeeeeeebbbbbccceee
        bccccffccceecccccccccccccccccccccccccccccfffffffffffffffffffffffcfccccccfcffccffffffffcffcfceccccceeeecccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebebbcccceee
        bcccfcfccceeccfccccccccccccccccccccccccccfffffffffffffffffffffffcfffcccfffffffffffffffffcffcccccccceeccccccceeeeecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccce
        cccccfffccccfffcccccccccccccccccccccfccccfffffffffffffffffffffffffffcccffffffffffffffffffffffccfffceecccccccceeecccceeecccceeeeeeeeeeeeeeeeeeeeeeeeeecccccccccee
        cccccfffffffffccccccccffccccccccccffffffffffffffffffffffffffffffffcfffcfffffffffffffffffffffffffffccecfccfcccccccffcccccffcceeccceeecccffceeeeeeeeeeccccccccccee
        """))
    reyStoryImg = img("""
        ......................................................eeeeeeee................................
        .....................................................eeeeeeeeee...............................
        ..................................................eeeeeeeeeeeeeee.............................
        ................................................eeeeeeeeeeeeeeeeeee...........................
        ...............................................eeeeeeeeeeeeeeeeeeeee..........................
        .............................................ceeeeeeeeeeeeeeeeeeeeeee.........................
        ............................................eeeeeeeeeeeeeeeeeeeeeeeeed........................
        ...........................................eeeeeeeeeeeeeeeeeeeeeeeeeeed.......................
        ...........................................eeeeeeeeeeeeeeeeeeeeeeeeeeee.......................
        ..........................................eeeeeeeeeeeeeeeeeeeeeeeeeeeeed......................
        ..........................................eeeeeeeeeeeeeeeeeeeeeeeeeeeeee......................
        ..........................................eeeeeeeeeeeeeeeeeeeeeeeeeeeeee......................
        ..........................................ceeeeeeeeeeeeeeeeeeeeeeeeeeeeee.....................
        ..........................................beeeeeeeeeeeeeeeeeeeeeeeeeeeeee.....................
        .........................................bbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee....................
        ..........................................ceeeebeeeeeeeeeeeeeeeeeeeeeeeeee....................
        ..........................................dddccbeeeeeeeeeeeeeeeeeeeeeeeeee....................
        .........................................bcddcddddeeeeeeeeeeddeeeeeeeeeeee....................
        ..........................................cddcddddddddddddddddeeeeeddddeee....................
        .........................................ddddddffccdddddddddddcfcbdddddeee....................
        .........................................fddddddcfffddddddddcfcbdbddddddee....................
        .........................................fdddddddddccddddddccdddddddddddee....................
        .........................................fddddddddddcdddddddddddddddddddcc....................
        .........................................fdddddddddddddddddddddddddddddddd....................
        .........................................fdddddddddddddddddddddddddddddddd....................
        ........................................bcddddcccccddddddddddccccddddddddd....................
        .......................................ffcddddccbbcfddddddddccbbccdddddddd....................
        .......................................fdddddddfcccccddddddddccfcddddddddd....................
        .......................................fdddddddddddddddddddddddddddddddddd....................
        .......................................fddddddddddddddddddddddddddcdddddd.....................
        ........................................fddddddddddddddddddddddddcdddddd......................
        ........................................fddddddddddddddddddddddddddddddd......................
        .........................................fcddddddddddddddddddddddddddddd......................
        ..........................................cdddddddddcddddddddddddddddddd......................
        ..........................................cdddddddddcdddddddddddddddddd.......................
        ...........................................dddddddddddddddddddddddddddd.......................
        ...........................................ddddddddccdddddddddddddddddd.......................
        ...........................................dddddddddddddddddddddddddddd.......................
        ...........................................dddddddddddddddddddddddddddd.......................
        ...........................................dddddddddddddddddddddddddddd.......................
        ...........................................cddddddddddddddddddddddddddd.......................
        ............................................cdddddddddddccccccdddddddc........................
        ............................................cbdddddddbcccccccdddddddd.........................
        ............................................ccbddddddcfcdddddddddddbc.........................
        ..............................................bddddddddddddddddddddb..........................
        ..............................................ccddddddddcdcfddddddbc..........................
        ...............................................ccddddddfccddddddddc...........................
        .................................................ddddddddddddddddc............................
        ..................................................dddddddccddddddc............................
        ..................................................cbddddddddddddfcb...........................
        ...................................................cbddddddddddcdd............................
        ....................................................ccdddddddccffddc..........................
        .....................................................ccdddddcfccbddc..........................
        .....................................................bddddddcbbdddbc..........................
        .....................................................ddbccdddddddddcc.........................
        .fffffffdf..........................................cddddddddddddddd..........................
        .fbfdfbfddf.........................................ccddddddddddddddcdddddddd.fffffffff.ff....
        .f.dddffddf.ff.......................................cddddddddddddddddccdddddff1111111ffff....
        .fffddddddddd.........................ff............ccdddddddddddddddddddddddff1111111111f....
        ..ff.dddddddd........................f.f..........ffdddddddddddddddddddddddddff1111111111f....
        fffffdddddddddd.....................f11.fff.fffffffdddddddddddddddddddddddddfff11111111111f...
        fdddddddddddddd.....................f1111.fffddddddddddddddddddddddddddddddddff11111111111f...
        ffddddddddddddf11..................f11111ffdddddddddddddddddddddddddddcdddddfb111111111111ff..
        .ffffdddddddddf111fff.............ff111111fddddddddddddddcddddddddddddddddfffb1111111111111f..
        ...f.ddddddddf1111d1f.............f11111111cddddddddddddddddddddddddddddddf1111111111111111f..
        ....ddddddddff1111111f...........ff11111111cbddddddddddddddddddddddddddddff1111111111111111f..
        ...ffdddddddf111111111ff.........f1111111111fbdddcddddddddddddddddddddddff111111111111111111f.
        ....fffffdddf1111111111ff......f.f1111111111fbddddddddcdddddddddddddddddff1d1111111111111111f.
        ........ffdff11111111111fff....fff1111111111fffdddddddddcdddddddcdddddfff1d11111111111111111f.
        .........ff.1111111111111fff...fbf111111111111ffffdddddddccddddcbddddfff11111111111111111111f.
        ...........ff11111111111111ff..f11111111111111111bfffffddddddddddddccbf111d11111111111ff111ff.
        ...........ff1111111111111111fff1111111111111111111111fffddddddddddc1c1d11d111111111fffffffff.
        ..........f1111111111111111111f1111111111111111111111c1dfffdddddddd1111111111111111.ffffffff..
        ..........f111111111111111111111111111111111111111111111fbfffffddddcc11111111111111fffff......
        ..........f1111111111111111111111111111111111111111111111ff11dfffff1111111111111111f..........
        ..........f11111111111111111111111111111111111111111111111111111f111111111111111111f..........
        ..........f111111111111111111111111111111111111111111111111111111111111111111111111f..........
        ..........f111111111111111111111111111111111111111111111111111111111111111111111111bf.........
        .........ff111111111111111111111111111111111111111111111111111111111111111111111111.f.........
        .........f11111111111111111111111111111111111111111111111111111111111111111111111111f.........
        .........ff111111111111111111111111111111.f111111111111111111111111111111111111d11dff.........
        ..........fffffffffff1111111111111111111fff1111111111111111111111111111111111111d1ff..........
        .....................ff11ff111111111111ff.11111111111111111111111111111111111111fff...........
        ......................ffffffffff111111fff.111111111111111111111111111111111111fff.............
        ...............................ffffffff.ff111111111111111111111111111111111bbff...............
        .........................................ff11111111111111111111111111111bbbfff................
        ..........................................fffffff1111111111111111111111bfff...................
        .............................................bbbbfffff111111111111111ffffb....................
        ................................................bbbbbbffffffffffffffff........................
        .....................................................bbbbbbbbbbbf.............................
        """)
    princesaStoryImg = img("""
        99999999999999999999999999999999999999999bbbb999999999999999999999999999999999999999999
        99999999999999999999999999999999999999bbbeeeeee9999999999999999999999999999999999999999
        9999999999999999999999999999999999be9beeeeeeeeeeb99999999999999999999999999999999999999
        99999999999999999999999999999999beeebebebbecbeeeeeb999999999999999999999999999999999999
        9999999999999999999999999999999eeebbeebeebeebbeeeeeb99999999999999999999999999999999999
        999999999999999999999999999999beeebeeebeebeeebeeeeee99999999999999999999999999999999999
        99999999999999999999999999999beeeeeeeebeebbeebbeeeeee9999999999999999999999999999999999
        9999999999999999999999999999beeeeeeeeebeebbeeeeeeeeeeb999999999999999999999999999999999
        999999999999999999999999999ceeeeeeeeeebeeebeeeeeeeeeeeb99999999999999999999999999999999
        999999999999999999999999999beeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999999999999999999999
        99999999999999999999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeb9999999999999999999999999999999
        99999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeebeeb999999999999999999999999999999
        9999999999999999999999999beeeeeeeeeeeeeeeeeeeeeeeeeeebeeb999999999999999999999999999999
        999999999999999999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeebeeeb99999999999999999999999999999
        999999999999999999999999beeeeeeeeeeeeeeeeeeeebbeeeeeeeeeeb99999999999999999999999999999
        999999999999999999999999eeeeeeeeeeeeeeeeeebcbbbbeeeeeeeeeb99999999999999999999999999999
        99999999999999999999999beeeeeeeeeebcbbebecbecbebbebeeeeeebb9999999999999999999999999999
        99999999999999999999999beeeeeeeeeebbbbbbbceeeeebbcbeeeeeebb9999999999999999999999999999
        9999999999999999999999bbeeeeeeeeebbbbbbbbbeeeeebbcebeeeeebe9999999999999999999999999999
        9999999999999999999999beeeeeeeebbbbbbebbbbeeeebbcbbbeeeeebeb999999999999999999999999999
        9999999999999999999999beeeeeeeebdbbbbebbbbbeebbbbbbeebeebeeb999999999999999999999999999
        9999999999999999999999bbeeeeeebbdbbbbebbbbceebcebbbbcbeebeeb999999999999999999999999999
        9999999999999999999999bbeeeeeebbdbebbbecbccbbbbebcbccceebeeb999999999999999999999999999
        9999999999999999999999eeeeeeeebbdbeebbfbbbbbcbbebfccccbbbeeb999999999999999999999999999
        9999999999999999999999eeeeeebbbbdbbbbbbbddbccbbcccccfcbcbbeb999999999999999999999999999
        9999999999999999999999bbbebbbcbbddbcbccbcbdccbbbcffcbfbbbbee999999999999999999999999999
        9999999999999999999999eeeebbbbcbddbffffccbdbbbddbfcccccbbbeeb99999999999999999999999999
        9999999999999999999999eeeecddbccddbfffcbcbdbcdbbdccbfcbccbeb999999999999999999999999999
        9999999999999999999999eeeecddbccbdbbffffbdbfbdbbdbbbbbbcceec999999999999999999999999999
        9999999999999999999999eeeecbdbbcbdddbcccdbcbddbbdbbcbbbbbeeb999999999999999999999999999
        99999999999999999999999eeebcdbcbdddbddbdddddddbdddbdbbbbbbbb999999999999999999999999999
        99999999999999999999999beeebcbccdddbcbddddddddbdddddbbcbbbbb999999999999999999999999999
        99999999999999999999999beebbbfccbddddddddddddbbdddddbbcbebbb999999999999999999999999999
        99999999999999999999999beebbbcbcdddddddddddddbbdddddbbbbebeb999999999999999999999999999
        99999999999999999999999beebccbbcdddddddddddddbbdddddbbbbebeb999999999999999999999999999
        99999999999999999999999beeebcbbbbddddddddddddbbdddddccbbbbbf999999999999999999999999999
        99999999999999999999999beeecbbbbbddddddddddddbbdddddccbbbbef999999999999999999999999999
        99999999999999999999999beebbdbdbbddddddddddddbddddddccbbbeec999999999999999999999999999
        99999999999999999999999eeebbdbdbbdddddddddddddddddddcccbbeec999999999999999999999999999
        9999999999999999999999beeebbbbdbcddddddddddddddddddbcbceeeec999999999999999999999999999
        9999999999999999999999beeebbccbbcddddddddddddddddddbcbbbbbeb999999999999999999999999999
        9999999999999999999999beeebcbcbbcdddddddddddddddddbcebbccbeb999999999999999999999999999
        9999999999999999999999beeebcbcbbbbdddddddbcbbdddddcbebbbcbebb99999999999999999999999999
        9999999999999999999999bbeeebcccbbcddddddcfbbccdddbceebbbbeebb99999999999999999999999999
        999999999999999999999cebeeebcfccbcbddddddbbbbbddbceeeeeeeeeeb99999999999999999999999999
        999999999999999999999beeeeeeebbccffbddddbbbbbbdbcbeeeeeeeeeeb99999999999999999999999999
        999999999999999999999beeeeeeeeeebcffbddddbbbcbbbceeeeeeeeeeeb99999999999999999999999999
        999999999999999999999cebbeebeebbeeccbcbbdddddbcceeeeeeeeebbeb99999999999999999999999999
        999999999999999999999bebeeeeeeeeeeecbbbbbbbbbcceeeeeeeeeeecbb99999999999999999999999999
        999999999999999999999bebeeeeeeeeeeebcbbbbbccccbeeeeeeeeeeeb99999999999999999999999db999
        99999999999999999999cbbbbeebeeeeeeebcbbbbbbdbcbeeeeeeeeeec99999999999999999999999dbcb99
        99999999999999999999cbbbbbbbbeebeeebcbbbbbbdbceeeeeeeeeeecf999999999999999999999ddcbdb9
        99999999999999999999bbbbbeebeeeeeeeebddddbbbbceeeeeeeeeeebf99999999999999999bd99d..ddc9
        9999999999999999999bbbbbeeeeeeeeeeeecdddddbdbceeeeeeeeeeeb999999999999999999bd9bd...bb9
        9999999999999999999ccbbbbbbbbbbbbbbfbddddddddcbeeeeeebeeeeb99999999999999999bbcdd..cbd9
        9999999999999999999fcccccbbbbcccbbbbdddddddddbbeeeeeeeeeeeb99999999999999999dbcbd..bdbb
        9999999999999999999cccbbbddbdbfbddddddddddddddcbeeeeeeeeeeb9999999999999999bddbcd.ddbbd
        99999999b9999999999fcddbbbdddbfbbbbccccddddddddbcbeeeeeeeeb9999999999999999bdddbdddbdd9
        9999bb99bb999999999cbbbddddddcccbbbbbdbcbdbbcbbddbbbbbbbeb99999999999999999bddddddddd99
        bb99bb99bb999999999bdddddddddbbcdddddddbddbcbbccbbbcccbbbc9999999999999999bddddddddb999
        9bbccbbfbdb99999999bbddddddcb11cbdddddddddddddddbbbccbddddd99999999999999bddddddddc9999
        9cbbbdbbbbbb9999999ddddddddb111bcbddddddddddddddddcccbdddddd999999999999cddbbddbbc99999
        9dcbbbbbbbbbb99999bddddddcdbb111bcbddddddddddddddbb1cbddddddd99999999999bdddddbcc999999
        99bbbbbbdbbbb99999bdddddcddb11111bcbddddddddddddbcb1cbdddddddb999999999bddddddc99999999
        99bbbbbbbbbbbb9999bdddddcddb1111111ccbdddddddddbcb11cbdddddddb99999999bddddddb999999999
        9bbbbbbbbbbbbbb999bddddddddbbb111111bccbbddddbbbcb11bbdddbddddb9999999bdbddddc999999999
        999ccbbbbbbbbbdb99bddddcdddbb111111111bbbbbbbbcbd11111ddddddddb999999bddbdddb9999999999
        999999bccbbbbbbb99bddddcdddbd1111111111111111111111111bddddddddc99999dddddddc9999999999
        99999999cbbbbbbbbfbddddcdddbb1111111111111111111111111bdbbdddddb9999bdddbddb99999999999
        999999999cbbbbbbbcbbdddcdddbb1111111111111111111111111cbbbdddbdb9999bdddbddc99999999999
        9999999999bdbbbbbbbddddcddddb1111111111111111111111111bcbddddddbd99bddddbdb999999999999
        99999999999bbbbbbbcbddddddddb1111111111111111111111111bfbddddddbb99bddddddc999999999999
        99999999999bdbbbbbbcbdddddbbb111111111111111111111111bbfbbddbbdbb9bdbbbbbb9999999999999
        999999999999bbbbbbbcbdddcbbbb111111111111111111111111bb9bddddbdbbcbdbbddbc9999999999999
        999999999999bbbbbbbbcdddcbdb1111111111111111111111111bc9bddddbddbbddbbddb99999999999999
        9999999999999bbbbbbbcbbdcbdb1111111111111111111111111bf99bdddbddcbddbbddc99999999999999
        9999999999999cbbbbbbcbbbcbbb11111111bbbb11bb1bb111b11c999bdbbbdbcbbbbbbb999999999999999
        99999999999999bbbbbbbbbbcbdb1111111b1111111111b11111b9999bddbbdbbbdbbbdc999999999999999
        99999999999999cbbbbbbbbbcbdb1111111b1111111111111111c9999cddbbdbbbbbbdb9999999999999999
        99999999999999cbbbbbbbbbcbbb1111111b111b111111b1111b999999bdbbdbbbbbbdc9999999999999999
        999999999999999cbbbbbbbbcbbbb11111bb111b11b111b111bc999999bdbbddbbbbbb99999999999999999
        9999999999999999bbbbbbdbcbddb1db111b11111111111111b99999999dbbddbbbbb999999999999999999
        9999999999999999cbbbbbbbbbbdbddb111b11111111111111c99999999bdbbbbbbdb999999999999999999
        99999999999999999cbbbbbcbbbbbbbbb11b111b11b111b11bc99999999bdbbbbbbbb999999999999999999
        999999999999999999bdbbb99bddbbdbb11b111b111111b111c999999999bbddbbbb9999999999999999999
        9999999999999999999bbbc999bbbddbb11b11111111111111c999999999bbbdbbbb9999999999999999999
        9999999999999999999999c99999bbdbb11b11111111111111c9999999999bbbbbb99999999999999999999
        99999999999999999999999999999cbb111bbbbb11bb11bb1bb9999999999bbbbbb99999999999999999999
        99999999999999999999999999999999bb111111111111111bc99999999999bdbb999999999999999999999
        999999999999999999999999999999999999bb1b11bbbbbcc999999999999999b9999999999999999999999
        """)
    encantaStorySprite = sprites.create(assets.image("""
        la encantá
        """), 0)
    reyStorySprite = sprites.create(reyStoryImg, 0)
    encantaStorySprite.set_position(40, 40)
    reyStorySprite.set_position(105, 40)
    story.print_text("Hace muchos años en la localidad de Rojales",
        80,
        100,
        15,
        1,
        story.TextSpeed.FAST)
    story.print_text("Un rey malvado maldijo a su hija por enamorase de un príncipe extranjero",
        80,
        100,
        15,
        1,
        story.TextSpeed.FAST)
    reyStorySprite.destroy()
    story.print_text("La única manera de salvarla sería bañando sus pies en el rio Segura",
        80,
        100,
        15,
        1,
        story.TextSpeed.FAST)
    encantaStorySprite.destroy(effects.fire, 500)
    story.print_text("Por eso cada 100 años se aparece durante la noche de San Juan en el Cabezo Soler",
        80,
        100,
        15,
        1,
        story.TextSpeed.FAST)
    story.print_text("Años atrás un jornalero del pueblo la encontró y trató de salvarla...",
        80,
        100,
        15,
        1,
        story.TextSpeed.FAST)
    IrFase("story", "game")
multigame.on_start("story", on_on_start2)

def startGame():
    global velocidadSalto, aceleracionSalto, velocidadScroll, tioVilaSprite, fase
    velocidadSalto = -150
    aceleracionSalto = 310
    velocidadScroll = -50
    info.set_life(3)
    info.set_score(0)
    scene.set_background_image(img("""
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddd33dddddddddddddddddddddddddddddddddddddd33dddddddddddddddddddddddddddddddddddddd33dddddddddddddddddddddddddddddddddddddd33dddddddddddddddd
        ddddddddddddddddddddddd3ddddddddddddddddddddddddddddddddddddddd3ddddddddddddddddddddddddddddddddddddddd3ddddddddddddddddddddddddddddddddddddddd3dddddddddddddddd
        ddddddddddddddddddddd3333dddddddddddddddddddddddddddddddddddd3333dddddddddddddddddddddddddddddddddddd3333dddddddddddddddddddddddddddddddddddd3333ddddddddddddddd
        dddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddd
        ddddddddddddddddddd3333333ddddddddddddddddddddddddddddddddd3333333ddddddddddddddddddddddddddddddddd3333333ddddddddddddddddddddddddddddddddd3333333dddddddddddddd
        ddddddddddddddddddd33333d3ddddddddddddddddddddddddddddddddd33333d3ddddddddddddddddddddddddddddddddd33333d3ddddddddddddddddddddddddddddddddd33333d3dddddddddddddd
        ddddddddddddbddddddd3333ddddddddddddddddddddddddddddbddddddd3333ddddddddddddddddddddddddddddbddddddd3333ddddddddddddddddddddddddddddbddddddd3333dddddddddddddddd
        ddddddddddddbdddddd3333333ddddddddddddddddddddddddddbdddddd3333333ddddddddddddddddddddddddddbdddddd3333333ddddddddddddddddddddddddddbdddddd3333333dddddddddddddd
        ddddddddddddbddddd33333333ddddddddddddddddddddddddddbddddd33333333ddddddddddddddddddddddddddbddddd33333333ddddddddddddddddddddddddddbddddd33333333dddddddddddddd
        ddddddddddddbdddd33333333333ddddddddddddddddddddddddbdddd33333333333ddddddddddddddddddddddddbdddd33333333333ddddddddddddddddddddddddbdddd33333333333dddddddddddd
        dd33ddddddddbdd3d3333333333333ddddbddddddd33ddddddddbdd3d3333333333333ddddbddddddd33ddddddddbdd3d3333333333333ddddbddddddd33ddddddddbdd3d3333333333333ddddbddddd
        d33333ddddddbdd333333333333333ddddbdddddd33333ddddddbdd333333333333333ddddbdddddd33333ddddddbdd333333333333333ddddbdddddd33333ddddddbdd333333333333333ddddbddddd
        33333333ddddbddd33333333333333ddddbddddd33333333ddddbddd33333333333333ddddbddddd33333333ddddbddd33333333333333ddddbddddd33333333ddddbddd33333333333333ddddbddddd
        333333333ddddbdddd333333333333ddddbddddd333333333ddddbdddd333333333333ddddbddddd333333333ddddbdddd333333333333ddddbddddd333333333ddddbdddd333333333333ddddbddddd
        d33333333dddddbdddd3333333444444dbbdddd3d33333333dddddbdddd3333333444444dbbdddd3d33333333dddddbdddd3333333444444dbbdddd3d33333333dddddbdddd3333333444444dbbdddd3
        d333333333dddddbb3333333444444444bdddd3dd333333333dddddbb3333333444444444bdddd3dd333333333dddddbb3333333444444444bdddd3dd333333333dddddbb3333333444444444bdddd3d
        33333333ddddddddbb33333333443443bbdddddd33333333ddddddddbb33333333443443bbdddddd33333333ddddddddbb33333333443443bbdddddd33333333ddddddddbb33333333443443bbdddddd
        333333333dddddd333b333333343334bb3ddddd3333333333dddddd333b333333343334bb3ddddd3333333333dddddd333b333333343334bb3ddddd3333333333dddddd333b333333343334bb3ddddd3
        3333b33dddddd33333333333333333bbdddddd333333b33dddddd33333333333333333bbdddddd333333b33dddddd33333333333333333bbdddddd333333b33dddddd33333333333333333bbdddddd33
        3333b3333ddddd333333333333333bbddddddd333333b3333ddddd333333333333333bbddddddd333333b3333ddddd333333333333333bbddddddd333333b3333ddddd333333333333333bbddddddd33
        3333b33b33dddddd333344444333333ddddddd333333b33b33dddddd333344444333333ddddddd333333b33b33dddddd333344444333333ddddddd333333b33b33dddddd333344444333333ddddddd33
        3333b33b33ddddd34444444444333333333ddd333333b33b33ddddd34444444444333333333ddd333333b33b33ddddd34444444444333333333ddd333333b33b33ddddd34444444444333333333ddd33
        3333b3b333dddd444444444443344433333ddd333333b3b333dddd444444444443344433333ddd333333b3b333dddd444444444443344433333ddd333333b3b333dddd444444444443344433333ddd33
        3333bbb3443d3334444444444443444333ddddd33333bbb3443d3334444444444443444333ddddd33333bbb3443d3334444444444443444333ddddd33333bbb3443d3334444444444443444333ddddd3
        3333bb3443334444444444444444344433dddd333333bb3443334444444444444444344433dddd333333bb3443334444444444444444344433dddd333333bb3443334444444444444444344433dddd33
        333bb33333444444444444444444433333333333333bb33333444444444444444444433333333333333bb33333444444444444444444433333333333333bb33333444444444444444444433333333333
        33bb333344444444444444443bb333333333b33333bb333344444444444444443bb333333333b33333bb333344444444444444443bb333333333b33333bb333344444444444444443bb333333333b333
        33b3333433334443443443443bb333443333b33333b3333433334443443443443bb333443333b33333b3333433334443443443443bb333443333b33333b3333433334443443443443bb333443333b333
        33b3b33333344434433444333bb333b44333b33333b3b33333344434433444333bb333b44333b33333b3b33333344434433444333bb333b44333b33333b3b33333344434433444333bb333b44333b333
        3bb3b33333343334333334333bb333b33333b3333bb3b33333343334333334333bb333b33333b3333bb3b33333343334333334333bb333b33333b3333bb3b33333343334333334333bb333b33333b333
        3bbbb33333333433344333333bb333b333333b333bbbb33333333433344333333bb333b333333b333bbbb33333333433344333333bb333b333333b333bbbb33333333433344333333bb333b333333b33
        3bbb333333334433443333333bb333b333333b333bbb333333334433443333333bb333b333333b333bbb333333334433443333333bb333b333333b333bbb333333334433443333333bb333b333333b33
        3b333333333343333333b3333bb33b3333333bbb3b333333333343333333b3333bb33b3333333bbb3b333333333343333333b3333bb33b3333333bbb3b333333333343333333b3333bb33b3333333bbb
        bb333333333333333333b3333bbb3b333333333bbb333333333333333333b3333bbb3b333333333bbb333333333333333333b3333bbb3b333333333bbb333333333333333333b3333bbb3b333333333b
        3b333333333333333333b3333bbbb333333333333b333333333333333333b3333bbbb333333333333b333333333333333333b3333bbbb333333333333b333333333333333333b3333bbbb33333333333
        3b333333333333333333b3333bbbb333444333333b333333333333333333b3333bbbb333444333333b333333333333333333b3333bbbb333444333333b333333333333333333b3333bbbb33344433333
        3b444334443333333333b3333bbb3334443333333b444334443333333333b3333bbb3334443333333b444334443333333333b3333bbb3334443333333b444334443333333333b3333bbb333444333333
        44444433444333333333b3333bbb33444334444444444433444333333333b3333bbb33444334444444444433444333333333b3333bbb33444334444444444433444333333333b3333bbb334443344444
        44443333b44433333333b3333bbb33333444444444443333b44433333333b3333bbb33333444444444443333b44433333333b3333bbb33333444444444443333b44433333333b3333bbb333334444444
        44444443b33333333b33b3333bbb33334444444444444443b33333333b33b3333bbb33334444444444444443b33333333b33b3333bbb33334444444444444443b33333333b33b3333bbb333344444444
        44444444443333333b33b3333bbbb3444434444444444444443333333b33b3333bbbb3444434444444444444443333333b33b3333bbbb3444434444444444444443333333b33b3333bbbb34444344444
        44444344443333333b33b3333bbb4444b433443444444344443333333b33b3333bbb4444b433443444444344443333333b33b3333bbb4444b433443444444344443333333b33b3333bbb4444b4334434
        3444333bb3bb33333b33b3333bbbb444b33443333444333bb3bb33333b33b3333bbbb444b33443333444333bb3bb33333b33b3333bbbb444b33443333444333bb3bb33333b33b3333bbbb444b3344333
        33b4333bb3b333333bb3bb333bbbb333bb33333333b4333bb3b333333bb3bb333bbbb333bb33333333b4333bb3b333333bb3bb333bbbb333bb33333333b4333bb3b333333bb3bb333bbbb333bb333333
        33b3333bbbb3333333bbbb333bbbb333bb33333333b3333bbbb3333333bbbb333bbbb333bb33333333b3333bbbb3333333bbbb333bbbb333bb33333333b3333bbbb3333333bbbb333bbbb333bb333333
        33b3333bb3333333333bbb333bbbb333bb33333333b3333bb3333333333bbb333bbbb333bb33333333b3333bb3333333333bbb333bbbb333bb33333333b3333bb3333333333bbb333bbbb333bb333333
        33b3333bb33333333333bbb33bbbb333bb33333333b3333bb33333333333bbb33bbbb333bb33333333b3333bb33333333333bbb33bbbb333bb33333333b3333bb33333333333bbb33bbbb333bb333333
        333b333bb33333333333bbb33bbbb333bb333333333b333bb33333333333bbb33bbbb333bb333333333b333bb33333333333bbb33bbbb333bb333333333b333bb33333333333bbb33bbbb333bb333333
        333bb3bbb3333443444334b33bbbb333bb33b333333bb3bbb3333443444334b33bbbb333bb33b333333bb3bbb3333443444334b33bbbb333bb33b333333bb3bbb3333443444334b33bbbb333bb33b333
        333bbbbbb3334444444444443bbbbb33bb33b333333bbbbbb3334444444444443bbbbb33bb33b333333bbbbbb3334444444444443bbbbb33bb33b333333bbbbbb3334444444444443bbbbb33bb33b333
        3333bbbbb334444444444444bbbbbb3bb33bb3333333bbbbb334444444444444bbbbbb3bb33bb3333333bbbbb334444444444444bbbbbb3bb33bb3333333bbbbb334444444444444bbbbbb3bb33bb333
        33333bbbb333443444444434bbbbbb3bb33b333333333bbbb333443444444434bbbbbb3bb33b333333333bbbb333443444444434bbbbbb3bb33b333333333bbbb333443444444434bbbbbb3bb33b3333
        33333bbb3344334444443433bbbbbb3bb3b3333333333bbb3344334444443433bbbbbb3bb3b3333333333bbb3344334444443433bbbbbb3bb3b3333333333bbb3344334444443433bbbbbb3bb3b33333
        33333bbb3333344334433433bbbbbb3bbb33333333333bbb3333344334433433bbbbbb3bbb33333333333bbb3333344334433433bbbbbb3bbb33333333333bbb3333344334433433bbbbbb3bbb333333
        33333bbb333b3433333333333bbbbbbb3333333333333bbb333b3433333333333bbbbbbb3333333333333bbb333b3433333333333bbbbbbb3333333333333bbb333b3433333333333bbbbbbb33333333
        33333bbb333b3333333333333bbbbbbb3333333333333bbb333b3333333333333bbbbbbb3333333333333bbb333b3333333333333bbbbbbb3333333333333bbb333b3333333333333bbbbbbb33333333
        33333bbb333b3b33333333333bbbbbbb3333333333333bbb333b3b33333333333bbbbbbb3333333333333bbb333b3b33333333333bbbbbbb3333333333333bbb333b3b33333333333bbbbbbb33333333
        33333bbb333b3b33333333333bbbbbb33333333333333bbb333b3b33333333333bbbbbb33333333333333bbb333b3b33333333333bbbbbb33333333333333bbb333b3b33333333333bbbbbb333333333
        33333bbb333b3b33333333333bbbbb333333333333333bbb333b3b33333333333bbbbb333333333333333bbb333b3b33333333333bbbbb333333333333333bbb333b3b33333333333bbbbb3333333333
        33333bb3333bbb33333333333bbbbb333333333333333bb3333bbb33333333333bbbbb333333333333333bb3333bbb33333333333bbbbb333333333333333bb3333bbb33333333333bbbbb3333333333
        33333bb333bbb333333333333bbbbb333333333333333bb333bbb333333333333bbbbb333333333333333bb333bbb333333333333bbbbb333333333333333bb333bbb333333333333bbbbb3333333333
        3333bbb333b333333333dd333bbbbb3d333333333333bbb333b333333333dd333bbbbb3d333333333333bbb333b333333333dd333bbbbb3d333333333333bbb333b333333333dd333bbbbb3d33333333
        3333bbb333b3333333333dd3bbbbbb33dd3333d33333bbb333b3333333333dd3bbbbbb33dd3333d33333bbb333b3333333333dd3bbbbbb33dd3333d33333bbb333b3333333333dd3bbbbbb33dd3333d3
        3333bbb3bbb3333333333333bbbbbbb33d333dd33333bbb3bbb3333333333333bbbbbbb33d333dd33333bbb3bbb3333333333333bbbbbbb33d333dd33333bbb3bbb3333333333333bbbbbbb33d333dd3
        dd33bbbbbb33333333d33333bbbbbbb333333d33dd33bbbbbb33333333d33333bbbbbbb333333d33dd33bbbbbb33333333d33333bbbbbbb333333d33dd33bbbbbb33333333d33333bbbbbbb333333d33
        3dd3bbbbb33dd3333dd3333dbbbbbbbd333333333dd3bbbbb33dd3333dd3333dbbbbbbbd333333333dd3bbbbb33dd3333dd3333dbbbbbbbd333333333dd3bbbbb33dd3333dd3333dbbbbbbbd33333333
        3dddbbbbb333dd33dd33d3ddbbbbbbbd333d33333dddbbbbb333dd33dd33d3ddbbbbbbbd333d33333dddbbbbb333dd33dd33d3ddbbbbbbbd333d33333dddbbbbb333dd33dd33d3ddbbbbbbbd333d3333
        3dddbbb333333333d33dddddbbbbbbbdd3dd33d33dddbbb333333333d33dddddbbbbbbbdd3dd33d33dddbbb333333333d33dddddbbbbbbbdd3dd33d33dddbbb333333333d33dddddbbbbbbbdd3dd33d3
        ddddbbbd33333333333dddddbbbbbbbdddd33dddddddbbbd33333333333dddddbbbbbbbdddd33dddddddbbbd33333333333dddddbbbbbbbdddd33dddddddbbbd33333333333dddddbbbbbbbdddd33ddd
        ddddbbbd333d33ddd33dddddbbbbbbbdddddddddddddbbbd333d33ddd33dddddbbbbbbbdddddddddddddbbbd333d33ddd33dddddbbbbbbbdddddddddddddbbbd333d33ddd33dddddbbbbbbbddddddddd
        ddddbbbd33ddd3dddd3dddddbbbbbbbdddddddddddddbbbd33ddd3dddd3dddddbbbbbbbdddddddddddddbbbd33ddd3dddd3dddddbbbbbbbdddddddddddddbbbd33ddd3dddd3dddddbbbbbbbddddddddd
        ddddbbbdddddddddddddddddbbbbbbbdddddddddddddbbbdddddddddddddddddbbbbbbbdddddddddddddbbbdddddddddddddddddbbbbbbbdddddddddddddbbbdddddddddddddddddbbbbbbbddddddddd
        ddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbddddddddd
        ddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbddddddddd
        ddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbddddddddd
        ddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbddddddddd
        ddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbddddddddd
        ddddbbbb3dddddddddddddddbbbbbbbdddddddddddddbbbb3dddddddddddddddbbbbbbbdddddddddddddbbbb3dddddddddddddddbbbbbbbdddddddddddddbbbb3dddddddddddddddbbbbbbbddddddddd
        ddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbddddddddd
        ddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbddddddddd
        ddddbbbbb3ddddddddddddd3bbbbbbb3ddddddddddddbbbbb3ddddddddddddd3bbbbbbb3ddddddddddddbbbbb3ddddddddddddd3bbbbbbb3ddddddddddddbbbbb3ddddddddddddd3bbbbbbb3dddddddd
        ddddbbbbb3dddddddddddddbbbbbbbb3ddddddddddddbbbbb3dddddddddddddbbbbbbbb3ddddddddddddbbbbb3dddddddddddddbbbbbbbb3ddddddddddddbbbbb3dddddddddddddbbbbbbbb3dddddddd
        ddd3bbbbbbdddddddddddddbbbbbbbbbddddddddddd3bbbbbbdddddddddddddbbbbbbbbbddddddddddd3bbbbbbdddddddddddddbbbbbbbbbddddddddddd3bbbbbbdddddddddddddbbbbbbbbbdddddddd
        ddd3bbbbbbdddddddddddd3bbbbbbbbbddddddddddd3bbbbbbdddddddddddd3bbbbbbbbbddddddddddd3bbbbbbdddddddddddd3bbbbbbbbbddddddddddd3bbbbbbdddddddddddd3bbbbbbbbbdddddddd
        443bbbbbbb3dddddddddddbbbbbbbb4444444444443bbbbbbb3dddddddddddbbbbbbbb4444444444443bbbbbbb3dddddddddddbbbbbbbb4444444444443bbbbbbb3dddddddddddbbbbbbbb4444444444
        44444444bbbddddddddd33bbb44444444444444444444444bbbddddddddd33bbb44444444444444444444444bbbddddddddd33bbb44444444444444444444444bbbddddddddd33bbb444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        """))
    effects.star_field.start_screen_effect()
    tiles.set_current_tilemap(tilemap("""
        forest
        """))
    scroller.scroll_background_with_speed(velocidadScroll, 0)
    tioVilaSprite = sprites.create(img("""
            ..............................
            ..............................
            ..............................
            ..........fffff...............
            ..........fffdf...............
            ..........ffd1d...............
            ..........fd3fd...............
            ..........dddddeee............
            ...........d22eeeee...........
            .........dd9d2eeeee...........
            .........dd9ddeeeee...........
            .........dd999eeeee...........
            ..........ddd9eeeeee..........
            ..........9dddeeeeee..........
            ..........99dddd111...........
            ..........9999dd1991..........
            ..........eeee711111..........
            ..........99991111111.........
            ...........99911111111........
            ...........8999..d.d..........
            ...........88999..............
            .........e888.999.............
            .........e88...992............
            .........ee8...222............
            ..............................
            ..............................
            ..............................
            ..............................
            ..............................
            ..............................
            """),
        SpriteKind.player)
    animation.run_image_animation(tioVilaSprite,
        assets.animation("""
            player_sprite
            """),
        200,
        True)
    tioVilaSprite.set_position(15, 90)
    tioVilaSprite.ay = aceleracionSalto
    pause(1000)
    fase = "game"

def on_on_start3():
    pass
multigame.on_start("game", on_on_start3)

def RandomizeImage(background: Image):
    global tempBackground
    if initGame:
        tempBackground = background
        for index in range(15):
            tempBackground.replace(index, randint(0, 14))
        scroller.set_background_scroll_offset(0, 0)
        scene.set_background_image(tempBackground)
        
        def on_after():
            RandomizeImage(background)
        timer.after(3000, on_after)
        

def on_update_interval():
    if True:
        pass
multigame.on_update_interval("game", 1000, on_update_interval)

def on_a_pressed():
    if fase == "game":
        if tioVilaSprite.is_hitting_tile(CollisionDirection.BOTTOM):
            tioVilaSprite.vy = velocidadSalto
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(otherSprite)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def on_a_pressed2():
    pass
multigame.A.on_event("game", ControllerButtonEvent.PRESSED, on_a_pressed2)

def DelMenuFase():
    sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
    sprites.destroy_all_sprites_of_kind(SpriteKind.text)
    effects.star_field.end_screen_effect()
def InitMenuFase():
    global fase, titleTextSprite, myMenu
    fase = "menu"
    scene.set_background_image(img("""
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbdddbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcccfccccceeccbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbffccccccccceecceebdbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbfcccccccccccccceeeeeeeecccdddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbfccccccccccccccccccceeeeeecceebbddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcfccccccccccccccccccccccceeccceeefcdddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcfcccccccccccccccccccccccceeeccceeeeccddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbffccccccccccccccccccccccccceeeecceeeeeeebddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbffccccccccccccccccccccccccccceeeecccceeeeeeebddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbfffccccccccccccccccccccccccceeeeeeeeccccceeeeeeefbddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbcfccccccccccccccccccccccccccceebeeeeeccccfeeeeeeeeebdddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcfcccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeebdddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcccccccccccccccccccccccccccccccceeeeebeebeebbeeeeeeeeeeeeebddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcccccccccccccccccccccccccccccccccceeeeeeeeeebeeeeeebbeebeeeeebddddddddddddddddddddddddddddddddddddddddd
        bbbbbbbddddbbddbbbbdddddddddddddddddddddddddddddddddddbffcccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeebddddddddddddddddddddddddddddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbdddbddbdddddddddddddddddddddddddbfcccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeebdddddddddddddddddddddddddddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddbbbcfcccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeebddddddddddddddddddddddddddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcfcccccccccccccccccccccccccccccccccccccccceeeccceeeeeeeeeeeeeeeeeeeeeeeeeeeebddddddddddddddddddddbdddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbcccccccccccccccccccccccccccccccccccccccccceeecceeeceeeeeeeeeeeeeeeeeeeeeeeeeeebbdbbdddddbbbbbbbbdbdddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbfffccccccccccfcccccccccccccccccccccccccccccccceecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbdbbbbbbbbbbbbbbbbbbbbbbbdddbdd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcfcccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbdbbbbbbbbbbbbbbbbddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeccceeeeeeeeeeeeeeeeeeeeeeeeeeccbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbcbcbbccbbbccccccffccccccccccccccccccccccccfcccccccccccccccccccccccceeeeeeeeeeecceeeeeeeceeeeeeeeeeeeeeeeeeeeeeebbbbbbbccccccccccbcccbbbbc
        bbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccceeccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbccbcccb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccccccccecceeccceeeeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbbcccc
        cbccccccccbcbbbbcccccbbbbbbbcccfffcccccccccccccccccccccccccccccccccccffcccccccccccccccccceeeceeeeeeccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccbbbbbccc
        cccccbbbbbbbbbbcbcccccccffcfccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccceeeeceeeeeeceeeeeeeeeeeeeeeeeeeeeeeeecccceeeeeeeeeeeeccbbbccccccccccccc
        cbccccbbbbbbcbbcccccccccccccccccccccccccccffccfcfcccccccccccfffccccccccccccccccccccccccccceeeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccebeeeeeeeeeeeeeccccccccccccccc
        cccccbcccccccffcfffcccccccccccccccccccccccccccfcccccccccccccccccccccccccccccccccccccccecccceeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecceeeeeeeeeeeeeeccccccccccc
        ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccceeccccccccccccccceeccccceeeeeeeeeeeeeeeeeeeceeeeeeeeeccccceeeeeeccceeeeeeeeeeeeeecccccbcccc
        ccccccccccccccccccccccccccccccccccccccccccfcccfcccfffffcccccccccccccceeeeeecccceecccfcceecfcccceeeeeeeeeeeeeeeeccceeeeeccccccceeeeeeeecceeeeeeeeeeeeeeeecccccccc
        cccccccccccccccccccccccccccfcccfcccccccccccccfffcccccccccccccccccccccceebeebeecccccccfceeeecccceecccceeeeceeeeeeceeeeeeeeccccceeeeeeeeeceeeeeeeeeeeeeeeeeeeeeecc
        ccccccccccccccccccccccccccccfffccccccfffcccccccccccccccccfccccccccccccbbbebbebeeccccccceeeeeccceefcccceecceeeecceeeeeeccceeecceecceeeeeceeeeeeeeeeeeeeeeeeeeeeee
        cccccccccccccccccccccccccccccccccfcccfcccccffcccccccccccccccccccccccccceebbeebbeeeeeeeeeeeeeeceeecccccccccceeeeeeeeeccccceeecceeccfcceeeeeecceeeeeeeeeeeeeeeeeee
        cccccccccccccccccccccccccccccccccccccccfffffffcccfccccccccccffcccccccceeebbeebbeeebeeeeeeeeeeeeeeeeccccccccccecceeeeeccccceeecceeeeeeeeeeeeeeeeeeceeeeeeeeeeeeee
        ffccfffccccccccccfccccccfcccccfccffccffffccccfcccccffcccfcfcccffcccccceeeccceebeeebeeeeeeeeeeeeeebeeecceeecccccccceeeecccceeeeeeeeeebeeceeeeeeeecceeeeeeeeceeeee
        ccccccccccfffcccccccccccccfccccffffccccccccccccccccccccccfcccffffccccceecccceeeeeeebefeeeeeeeeeeeeeeeeeeecccccccceeeececeeeeeeeeefeeeeecceeeeeeeeceeeeeeeeeeeeee
        ccccccccffcccccccccccccccfccccfffccccccccccccfccccccfcccfcccfccccccccceecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecffccccceeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeeebeeeeeeeee
        ccccccccfcccccccccccccccccfffffcccccfccfffffcccccccccccfcccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        ccccffccccccccccccccfffcccccccccfccccfffffccccccccfccfffccccffcccccccccccccceebeeeeeeeeeebeeeeeeeeeeeeeeeecceeeccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        ccccccccccffccccccccfffccffffccccccfffcffccccfcccfcffccffcfffcccccccccccfffcceeeeceeeeeeeeebbeeeeeeeeeeeeeceeeeeceeeeeeebeeeeeeeeeeeeeeeeeeeeeeeceeeeeeeeeeeeeee
        cffcccfcffccccccccccccccffcffcfffffffccfffcffccccccccccfffcccfcccccccccccccccceeeeeccceeeeeeeeeeeeccceeeeceeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeeeccccccccceeeeeeeee
        cccccfffffcccccffccccfcfffffffffffffcccffcffccccccffffffcccccccccccccceecccccceeeeeecceeeeeeeeeeeccfccceeeeeeeeeeefeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccceeeeeeee
        ccccccfffcccccfcccccccccccfcffccccccccccccfccccccfcffcccfffcccccccccccceeccccccceeeecceeeeeeeeeeeecfcccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccceeeeecc
        fccccccccffccfccfcffffffccccffcccfccccccffcfcccffcfcfccfffcccccccccccccceecccccccceeeeeceeeeeeeeeeeccccccceeeeeeeeeeeeeeeeeeeeeeeeeeecceeeeeeeeceeeceecccceeeece
        cccccffccfccfffffffccfccccccccccccffcfccfcfccffffcffcccccfccccccccccccccccceccccccceeeeeeeeeeeeeeeeeeeecccceeeeeeeeeeeeeeeeeeeeeeeeeeeccceeeeeeeeeeeeeccceeeeeee
        ffccfffffffffffffffccfccccccccfcccccfcfffffcccffffcccfccffccccccccfccccccccceeccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccceeeeeeeeeeeccfceeeeee
        fffffffffffffffffffffffcccffccffffcccfcccccccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeebccceeeeeeeeeeeeeeeeeeeeeeeeecccceeeeeeeeecccceeeeee
        ccfffffffffffffffffffffccfffffffffffffccccccccccccccfccccccccccccccccccccccccccccccccccccccccccceccecceeeeccccccccceeeeecceeeeeeeceeeeeeeecccceeeeeeeecccccecccc
        ffffffffffffffffffffcffffffffcffffcffcccccccfcccffffffccccccccccccccccccccccccccccffcfffcccccfcccfcccccccefccccccccccccccccecceeeccceeeceeeccccceeeeeccccccccccc
        ffffffffffffffffffffffffffffffffffffcfffffffcccffffcccccfccffffccccfffccfffccffcccccccccccccccccccccccccceeccccfcccccccccccccceeeeffcccceecccccccccccccceccecccc
        fffffffffffffcfcfffffffffffffcffffffffcffccfcfffffcccccfffccccfcfffffcccffccfccccffcccccfccccccccccccfffcccceeccccccccffcfcccccceeccccccccfffcffcccccccceeeecccc
        fffffffffffffffcffffffffcfccffffffcffccffccccfcfcffffccccfccfccfffcffcccfccfcccccfccfccfffcccccccccccfffffceefcccccccffffccccfccceeccfffcccccccccccccccceeeeeecf
        ffffcffffccfffffffffffcfcccffffffffffffccccffffcccffceecfccfffffcccfcccccceccccccccccccccfffcffccccccffffceeeccccccccffccecccffccceeecffccccccccccccccceeeeeeccc
        ccffcccffffffffffffffccffcffccffffffcfccccfffcffccccceecccccccfccccffffcfccccfccccccccccccfffffcccfcccffffccccffffffcfccccccffffccceeccfcccffcfccccccceeeeeeccfc
        fcfccccffffffffffffffffcfffcfffffffccfcccfffccccccccceeeeeccccfccfffffffffcffffccecffceeeeccfcceecccfffcfffffffffffffffffccfffffffcccfcffcfffffcccceeefeeeeeeecf
        fcceeecfffffffffffffffffffffffffffccccccfccccecccccceeeeeeeeeffcffffffffffcfffffeeeecceeeeeeeceeeccccffcccfffffffffcffffcfcfffcfffffffffffffffffffceecceeeeeeeee
        ccceeeecccccccccfcfcffffccccffffcfcccfffffcceeeccccceeeeeeeeeeccfffffffcfcfffccfeeeeeceeeeeeeeeecffccffcffcffffffffcccffffccfcccfffffffccfffffffccfeefffceeeeeee
        fffeeeeeeeccccccccccfffcffcffcfffcfffceeefccffcccccceeeeeeeeeeecfffffccfffffffcceeeeeeecceeeeeeeecfffffffffffffffffffffffccfffcccccfffffffffffccccfcecfffcccceee
        cffeeeeeeeeefcfffffccfcccfcffcfcffccceeeeeeeeffffffffcccfeeeeeeccffccccecccccffcccceeeeccccceeeefecffffccfffffffcccffccffccfffffccccccffffffffcfcfffccfffccfccee
        eeeeeeeeeeeeecffffffccccccccccceccceeeeeeeeeeeeefccffccccfceeeeccceeeeeeeecccccccfceeefccffffccffeccffffffffffffccfffccfcccccffffcccfccffffcccfffffffccffccffccc
        eeeeeefeeeeeecfccccceeeeccccccceeeeeeecceceeeeeeccfffffcccccccccccceeccceecccccccfccecffffffffffcfcfcfccffcccccccccccccfcfccccffffffffffffcccefffffffffffffffccc
        eeeecffffffffffcccccfcfffccccfccceeeeefffffffffffffffffffffffffffffccfffeefcccfffffccccfffffccfffffcccecfcccccccccccffcffccffffcfffffffffffcfcffffffffffffffffcc
        eeeeffcfccffffffcfffffffffffcccffeeeeefffffffcffffccfffffffffffffccffffceefcffffffffffffffffcccffffcceeeccccccccccffffffffffffccfccffffffffffcffffffffffffffffcf
        eeeeccfeecffffffccffffffffffffccfeeeeecffffffffcfccffffffcffffffccccfccceeccccffcccffffffcffcccfccfccccccccccccccccfccfccfccfffcceefffffffffffffffffffffffffffcf
        eeeecffeeffffcffffffffffffffffccfffcecfffffffcccffffffffffffffffffccfccccccccccfccccffffffffffffffffffffffcccccccccfccceeeeccffffcecffffffffffffccccccccfffffffc
        eeeeffeeeffffffffffffffffffffccfffffffffffffffffffffffffffffffffffffcccffcccfccfccccfcfffffffffffffffffffffffccccfffcccfcffcffffffccccffffffffffccceeeeeefffffcc
        ceefffcecfffffffffffffffffffffffffffffffffffffffffffffffccfccfffffffffffffffffccfcfffffffffffffffffffffffffffffffffffffffffffffffcffccfffffffffffffcceeeeecfcfcc
        fffffffccccffffffffffffffffffffffffffffffffffffffffffffccccccccccccffffffffffffffffcffffffffffffffffffcfffcffffffffffffffffffffffcfffcccfffffffffffffffceececfcf
        ffffffffffccffffffffcccccfffffffffffffffffffffccccccccfcccccccccffffffffffffffffffffffffffffffffffffcfcfcccfffffffffffffffffffffffffffffffffffffffccfffccfeffccf
        fffffffffffffcccccccccccfffffffffffffffffffccccccccccccccccccccccfffffffffffffffffffcffffffffffffffffccccccfffffffffffffffffffffffffffffffffffffffcecffceeefcfff
        ffffffffffffcccccccccccccccccfffffffffccffcccccccccccccccccccccccccfffffffffffffffffcfffffffffffffffcffcccfffffffffffffffffffffffffffffffffffffffffeeeeeeeeeeeff
        ccccccccccccccccecccccccbccccfffccccffcccccccccccccccccccccccccccccfffffffffffffffffffffffffffffffffccfffffffffffffffffffffcffffffffffffffffffffffceeeeeeeeeeecf
        cccccccccccccccceeccccccccccccccccccffccbbccccccccccccccccccccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffccecfeeeeeeeff
        ccccccccccccccfceeeccccccccccccccccccfcccccccccccccccccccccccccccffffffffffffffffffffffffffffffffffffffffffffccffffffffffffffcffffffffffffffffffffffcccfeeeeefff
        cccccccccccccfcfceccccccccccccccccccccccccccccccccecccccccccccccccccfffffffffffffffffffffffffcfffffffffcffffccccccccccccfffffffffffffffffccfcfffffffffffceefffff
        cccccccccccfccffccfcccccccccccccccccccccccccceeeccecccccccccccccccccccccccccccccccccccccccccccccccccffccfffccccccccccccccccfccccccfffffccccccffffffffffffcffcffc
        cccccccccccffcfffffcccccccccccccccccccbbbcccceeeeeeeccccccccccccccccccccccccccccccccccccccccccccccccccccccccfcccccccccccccccccccccccccfcfffcffffffffffffffffffcf
        cccccccccccccfcccccccccccccccccccccccccbbcccceeeeeeeccceccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccffffffffffffffffffffffff
        ccccccccccccfffcccccccccccccccccccccccccccccceeeeeeeccceeeecccccccccccccccccccccccccccccccccccccccecccccccccccccccccccccccccccccccccccccfffffccfffffffffffffffff
        ccccccccccccccccccccccccccccccccccccccccccccceeeeeecccfeeeeeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccfffccccccccccccccccccccffffffffffcff
        cccccccccccccccccccccccccccccccccccccccccccceeeeeeeccffceeeeeebbbbbbbbcccccccccccccccccccccccceccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccffeeccccfeeeeeebbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbecccccccebbbccccccbcccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccbcccfffceecffceeeeeeccebbbbbbbbbbbbbbbbbbbbbcccccccebeecbeeeeebbbbbbbcccbbbbbbcccccccccccccccccccbbbccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccffffffeefffcffeeeeccbbbbbccccbbbbeebbeeebcccccccccccccceeebbeebbbbbbbebbbbebbbccccccccccccccbbbbbbbbbbbbbbbbccbbbbc
        cccccccccccccccccccccccccccccccccccccccbbbbccfffffceecfffffceeeccbbcbbbbcccceeeeeeeeeccccbcceeecccccceeeeeeeeecebbebbbbbbbeccbccccccccccbbbbbbbbbbbbbbbbbebbcccc
        cccccccccccccccfcccccccccccccccccccccccccccccfffffcffffffffffffccccccccccccccceeecffeeccebeeebeeeccccceebeeccccceeeeebbbbbbbbbbbbbbbbcccceeeebbeebbebbbbbccccccc
        cccccccccccccccfcccccccccccccccccccccccccccccffffffffffffffffcfffcccccccccccccffffffeecceeeebbbbeeeccceeeeeccccbeeeeeeebbbbcbbbbbbbbbbbbeebeeeeeeeeebebccbbbcccc
        cccccccccccccccfccccccccccccccccccccccccccccffffffffffffffffffffcccccbbcccccccffffffcfffeeeeebbbeeeecceeeeccccceeeeeeeebbbeecceeeeebbbecbbbbbbeeeeeeeeebbbebeeee
        cccccffccccecccccccccccccccccccccccccccccccffffffffffffffffffffccccccccccccfccffffffcffffceeeeeceeeeeeeeeccccceeeeeeeeeeeeeebbeeeeeebeeeeeeeeeeeeeeeebbbbbccceee
        bccccffccceecccccccccccccccccccccccccccccfffffffffffffffffffffffcfccccccfcffccffffffffcffcfceccccceeeecccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebebbcccceee
        bcccfcfccceeccfccccccccccccccccccccccccccfffffffffffffffffffffffcfffcccfffffffffffffffffcffcccccccceeccccccceeeeecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccce
        cccccfffccccfffcccccccccccccccccccccfccccfffffffffffffffffffffffffffcccffffffffffffffffffffffccfffceecccccccceeecccceeecccceeeeeeeeeeeeeeeeeeeeeeeeeecccccccccee
        cccccfffffffffccccccccffccccccccccffffffffffffffffffffffffffffffffcfffcfffffffffffffffffffffffffffccecfccfcccccccffcccccffcceeccceeecccffceeeeeeeeeeccccccccccee
        """))
    effects.star_field.start_screen_effect()
    titleTextSprite = textsprite.create("THE ENCANTÁ GAME")
    titleTextSprite.set_position(81, 14)
    myMenu = miniMenu.create_menu(miniMenu.create_menu_item("JUGAR"),
        miniMenu.create_menu_item("JUGAR SIN HISTORIA"),
        miniMenu.create_menu_item("CREDITOS"))
    
    def on_button_pressed(value, index2):
        if index2 == 0:
            DelMenuFase()
        if index2 == 1:
            DelMenuFase()
            startGame()
        if index2 == 2:
            IrFase("menu", "credits")
    myMenu.on_button_pressed(controller.A, on_button_pressed)
    
    music.play(music.string_playable("E B C5 A B G A F ", 120),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    music.set_volume(80)
# multigame.startGame("menu")

def on_on_score():
    startRio()
info.on_score(3, on_on_score)

def Flash_Outline():
    textSprite2.set_outline(1, 8)
    
    def on_after2():
        textSprite2.set_outline(1, 2)
        
        def on_after3():
            Flash_Outline()
        timer.after(100, on_after3)
        
    timer.after(100, on_after2)
    

def on_update_interval2():
    pass
multigame.on_update_interval("game", randint(1000, 2000), on_update_interval2)

def startRio():
    global tioVilaEndingSprite, encantaSprite, fase
    scroller.scroll_background_with_speed(0, 0)
    tiles.set_current_tilemap(tilemap("""
        nivel4
        """))
    tioVilaEndingSprite = sprites.create(img("""
            ..............................
            ..............................
            ..............................
            ..........fffff...............
            ..........fffdf...............
            ..........ffd1d...............
            ..........fd3fd...............
            ..........dddddeee............
            ...........d22eeeee...........
            .........dd9d2eeeee...........
            .........dd9ddeeeee...........
            .........dd999eeeee...........
            ..........ddd9eeeeee..........
            ..........9dddeeeeee..........
            ..........99dddd111...........
            ..........9999dd1991..........
            ..........eeee711111..........
            ..........99991111111.........
            ...........99911111111........
            ...........8999..d.d..........
            ...........88999..............
            .........e888.999.............
            .........e88...992............
            .........ee8...222............
            ..............................
            ..............................
            ..............................
            ..............................
            ..............................
            ..............................
            """),
        SpriteKind.player)
    tioVilaEndingSprite.set_position(15, 90)
    story.sprite_say_text(tioVilaEndingSprite, "No puedo más")
    encantaSprite = sprites.create(img("""
            ................
            .....eeeeee.....
            ....eeeeedee....
            ....ee1de1de....
            ....e3fddf3e....
            ....edddddde....
            ....eddfddde....
            ....eee22eee....
            ...eed1dd1dee...
            ...edd1111dde...
            ...ddd1111ddd...
            ..ddde1111eddd..
            ..dd..1111..dd..
            .....111111.....
            ....11111111....
            ......2222......
            ......dddd......
            ......dddd......
            .....dddddd.....
            ................
            """),
        SpriteKind.player)
    encantaSprite.set_position(55, 60)
    encantaSprite.ay = 200
    story.sprite_say_text(encantaSprite, "Te maldigo a morir con la lengua fuera")
    pause(2000)
    fase = "rio"
def RoleCredits():
    global textSprite2, textSprite, CharacterText, creditsIndex
    effects.star_field.start_screen_effect()
    textSprite2 = textsprite.create("CREDITOS")
    textSprite2.x += -20
    textSprite2.y = 120
    textSprite2.vy = -40
    pause(300)
    # Flash_Outline()
    textSprite2 = textsprite.create("")
    textSprite2.x += -50
    textSprite2.y = 60
    textSprite2.vy = -40
    # Flash_Outline()
    pause(500)
    while creditsIndex <= len(CreditsCharacters) - 1:
        textSprite = textsprite.create(CreditsCharacters[creditsIndex])
        textSprite.set_outline(1, 10)
        textSprite.vy = -40
        textSprite.y = 120
        textSprite.x += -40
        textSprite.set_flag(SpriteFlag.AUTO_DESTROY, True)
        pause(300)
        CharacterText = textsprite.create("(" + CreditsCharactersNames[creditsIndex] + ")")
        CharacterText.set_outline(1, 10)
        CharacterText.vy = -40
        CharacterText.y = 120
        CharacterText.x += -40
        pause(800)
        creditsIndex += 1
    pause(500)
    textSprite2.x += -40
    textSprite2.y = 120
    textSprite2.vy = -40
    textSprite2.set_flag(SpriteFlag.AUTO_DESTROY, True)
    # Flash_Outline()
    pause(1000)
    textSprite = textsprite.create("Gracias por todo")
    textSprite.set_outline(1, 10)
    textSprite.vy = -40
    textSprite.y = 120
    textSprite.x += -40
    textSprite.set_flag(SpriteFlag.AUTO_DESTROY, True)
    pause(2000)

def on_on_destroyed(sprite2):
    info.change_score_by(1)
sprites.on_destroyed(SpriteKind.projectile, on_on_destroyed)

def on_on_start4():
    pass
multigame.on_start("menu", on_on_start4)

def IrFase(currentFase2: str, newFase2: str):
    pass

def on_on_start5():
    global tioVilaStoryImg, tioVilaStorySprite
    scene.set_background_image(img("""
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbdddbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcccfccccceeccbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbffccccccccceecceebdbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbfcccccccccccccceeeeeeeecccdddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbfccccccccccccccccccceeeeeecceebbddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcfccccccccccccccccccccccceeccceeefcdddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcfcccccccccccccccccccccccceeeccceeeeccddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbffccccccccccccccccccccccccceeeecceeeeeeebddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbffccccccccccccccccccccccccccceeeecccceeeeeeebddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbfffccccccccccccccccccccccccceeeeeeeeccccceeeeeeefbddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbcfccccccccccccccccccccccccccceebeeeeeccccfeeeeeeeeebdddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcfcccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeebdddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcccccccccccccccccccccccccccccccceeeeebeebeebbeeeeeeeeeeeeebddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcccccccccccccccccccccccccccccccccceeeeeeeeeebeeeeeebbeebeeeeebddddddddddddddddddddddddddddddddddddddddd
        bbbbbbbddddbbddbbbbdddddddddddddddddddddddddddddddddddbffcccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeebddddddddddddddddddddddddddddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbdddbddbdddddddddddddddddddddddddbfcccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeebdddddddddddddddddddddddddddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddbbbcfcccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeebddddddddddddddddddddddddddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcfcccccccccccccccccccccccccccccccccccccccceeeccceeeeeeeeeeeeeeeeeeeeeeeeeeeebddddddddddddddddddddbdddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbcccccccccccccccccccccccccccccccccccccccccceeecceeeceeeeeeeeeeeeeeeeeeeeeeeeeeebbdbbdddddbbbbbbbbdbdddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbfffccccccccccfcccccccccccccccccccccccccccccccceecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbdbbbbbbbbbbbbbbbbbbbbbbbdddbdd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcfcccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbdbbbbbbbbbbbbbbbbddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeccceeeeeeeeeeeeeeeeeeeeeeeeeeccbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbcbcbbccbbbccccccffccccccccccccccccccccccccfcccccccccccccccccccccccceeeeeeeeeeecceeeeeeeceeeeeeeeeeeeeeeeeeeeeeebbbbbbbccccccccccbcccbbbbc
        bbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccceeccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbccbcccb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccccccccecceeccceeeeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbbbbbbbbcccc
        cbccccccccbcbbbbcccccbbbbbbbcccfffcccccccccccccccccccccccccccccccccccffcccccccccccccccccceeeceeeeeeccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccbbbbbccc
        cccccbbbbbbbbbbcbcccccccffcfccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccceeeeceeeeeeceeeeeeeeeeeeeeeeeeeeeeeeecccceeeeeeeeeeeeccbbbccccccccccccc
        cbccccbbbbbbcbbcccccccccccccccccccccccccccffccfcfcccccccccccfffccccccccccccccccccccccccccceeeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccebeeeeeeeeeeeeeccccccccccccccc
        cccccbcccccccffcfffcccccccccccccccccccccccccccfcccccccccccccccccccccccccccccccccccccccecccceeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecceeeeeeeeeeeeeeccccccccccc
        ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccceeccccccccccccccceeccccceeeeeeeeeeeeeeeeeeeceeeeeeeeeccccceeeeeeccceeeeeeeeeeeeeecccccbcccc
        ccccccccccccccccccccccccccccccccccccccccccfcccfcccfffffcccccccccccccceeeeeecccceecccfcceecfcccceeeeeeeeeeeeeeeeccceeeeeccccccceeeeeeeecceeeeeeeeeeeeeeeecccccccc
        cccccccccccccccccccccccccccfcccfcccccccccccccfffcccccccccccccccccccccceebeebeecccccccfceeeecccceecccceeeeceeeeeeceeeeeeeeccccceeeeeeeeeceeeeeeeeeeeeeeeeeeeeeecc
        ccccccccccccccccccccccccccccfffccccccfffcccccccccccccccccfccccccccccccbbbebbebeeccccccceeeeeccceefcccceecceeeecceeeeeeccceeecceecceeeeeceeeeeeeeeeeeeeeeeeeeeeee
        cccccccccccccccccccccccccccccccccfcccfcccccffcccccccccccccccccccccccccceebbeebbeeeeeeeeeeeeeeceeecccccccccceeeeeeeeeccccceeecceeccfcceeeeeecceeeeeeeeeeeeeeeeeee
        cccccccccccccccccccccccccccccccccccccccfffffffcccfccccccccccffcccccccceeebbeebbeeebeeeeeeeeeeeeeeeeccccccccccecceeeeeccccceeecceeeeeeeeeeeeeeeeeeceeeeeeeeeeeeee
        ffccfffccccccccccfccccccfcccccfccffccffffccccfcccccffcccfcfcccffcccccceeeccceebeeebeeeeeeeeeeeeeebeeecceeecccccccceeeecccceeeeeeeeeebeeceeeeeeeecceeeeeeeeceeeee
        ccccccccccfffcccccccccccccfccccffffccccccccccccccccccccccfcccffffccccceecccceeeeeeebefeeeeeeeeeeeeeeeeeeecccccccceeeececeeeeeeeeefeeeeecceeeeeeeeceeeeeeeeeeeeee
        ccccccccffcccccccccccccccfccccfffccccccccccccfccccccfcccfcccfccccccccceecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecffccccceeeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeeebeeeeeeeee
        ccccccccfcccccccccccccccccfffffcccccfccfffffcccccccccccfcccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        ccccffccccccccccccccfffcccccccccfccccfffffccccccccfccfffccccffcccccccccccccceebeeeeeeeeeebeeeeeeeeeeeeeeeecceeeccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        ccccccccccffccccccccfffccffffccccccfffcffccccfcccfcffccffcfffcccccccccccfffcceeeeceeeeeeeeebbeeeeeeeeeeeeeceeeeeceeeeeeebeeeeeeeeeeeeeeeeeeeeeeeceeeeeeeeeeeeeee
        cffcccfcffccccccccccccccffcffcfffffffccfffcffccccccccccfffcccfcccccccccccccccceeeeeccceeeeeeeeeeeeccceeeeceeeeeeeeeeeeeebeeeeeeeeeeeeeeeeeeeeeccccccccceeeeeeeee
        cccccfffffcccccffccccfcfffffffffffffcccffcffccccccffffffcccccccccccccceecccccceeeeeecceeeeeeeeeeeccfccceeeeeeeeeeefeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccceeeeeeee
        ccccccfffcccccfcccccccccccfcffccccccccccccfccccccfcffcccfffcccccccccccceeccccccceeeecceeeeeeeeeeeecfcccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccceeeeecc
        fccccccccffccfccfcffffffccccffcccfccccccffcfcccffcfcfccfffcccccccccccccceecccccccceeeeeceeeeeeeeeeeccccccceeeeeeeeeeeeeeeeeeeeeeeeeeecceeeeeeeeceeeceecccceeeece
        cccccffccfccfffffffccfccccccccccccffcfccfcfccffffcffcccccfccccccccccccccccceccccccceeeeeeeeeeeeeeeeeeeecccceeeeeeeeeeeeeeeeeeeeeeeeeeeccceeeeeeeeeeeeeccceeeeeee
        ffccfffffffffffffffccfccccccccfcccccfcfffffcccffffcccfccffccccccccfccccccccceeccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccceeeeeeeeeeeccfceeeeee
        fffffffffffffffffffffffcccffccffffcccfcccccccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeebccceeeeeeeeeeeeeeeeeeeeeeeeecccceeeeeeeeecccceeeeee
        ccfffffffffffffffffffffccfffffffffffffccccccccccccccfccccccccccccccccccccccccccccccccccccccccccceccecceeeeccccccccceeeeecceeeeeeeceeeeeeeecccceeeeeeeecccccecccc
        ffffffffffffffffffffcffffffffcffffcffcccccccfcccffffffccccccccccccccccccccccccccccffcfffcccccfcccfcccccccefccccccccccccccccecceeeccceeeceeeccccceeeeeccccccccccc
        ffffffffffffffffffffffffffffffffffffcfffffffcccffffcccccfccffffccccfffccfffccffcccccccccccccccccccccccccceeccccfcccccccccccccceeeeffcccceecccccccccccccceccecccc
        fffffffffffffcfcfffffffffffffcffffffffcffccfcfffffcccccfffccccfcfffffcccffccfccccffcccccfccccccccccccfffcccceeccccccccffcfcccccceeccccccccfffcffcccccccceeeecccc
        fffffffffffffffcffffffffcfccffffffcffccffccccfcfcffffccccfccfccfffcffcccfccfcccccfccfccfffcccccccccccfffffceefcccccccffffccccfccceeccfffcccccccccccccccceeeeeecf
        ffffcffffccfffffffffffcfcccffffffffffffccccffffcccffceecfccfffffcccfcccccceccccccccccccccfffcffccccccffffceeeccccccccffccecccffccceeecffccccccccccccccceeeeeeccc
        ccffcccffffffffffffffccffcffccffffffcfccccfffcffccccceecccccccfccccffffcfccccfccccccccccccfffffcccfcccffffccccffffffcfccccccffffccceeccfcccffcfccccccceeeeeeccfc
        fcfccccffffffffffffffffcfffcfffffffccfcccfffccccccccceeeeeccccfccfffffffffcffffccecffceeeeccfcceecccfffcfffffffffffffffffccfffffffcccfcffcfffffcccceeefeeeeeeecf
        fcceeecfffffffffffffffffffffffffffccccccfccccecccccceeeeeeeeeffcffffffffffcfffffeeeecceeeeeeeceeeccccffcccfffffffffcffffcfcfffcfffffffffffffffffffceecceeeeeeeee
        ccceeeecccccccccfcfcffffccccffffcfcccfffffcceeeccccceeeeeeeeeeccfffffffcfcfffccfeeeeeceeeeeeeeeecffccffcffcffffffffcccffffccfcccfffffffccfffffffccfeefffceeeeeee
        fffeeeeeeeccccccccccfffcffcffcfffcfffceeefccffcccccceeeeeeeeeeecfffffccfffffffcceeeeeeecceeeeeeeecfffffffffffffffffffffffccfffcccccfffffffffffccccfcecfffcccceee
        cffeeeeeeeeefcfffffccfcccfcffcfcffccceeeeeeeeffffffffcccfeeeeeeccffccccecccccffcccceeeeccccceeeefecffffccfffffffcccffccffccfffffccccccffffffffcfcfffccfffccfccee
        eeeeeeeeeeeeecffffffccccccccccceccceeeeeeeeeeeeefccffccccfceeeeccceeeeeeeecccccccfceeefccffffccffeccffffffffffffccfffccfcccccffffcccfccffffcccfffffffccffccffccc
        eeeeeefeeeeeecfccccceeeeccccccceeeeeeecceceeeeeeccfffffcccccccccccceeccceecccccccfccecffffffffffcfcfcfccffcccccccccccccfcfccccffffffffffffcccefffffffffffffffccc
        eeeecffffffffffcccccfcfffccccfccceeeeefffffffffffffffffffffffffffffccfffeefcccfffffccccfffffccfffffcccecfcccccccccccffcffccffffcfffffffffffcfcffffffffffffffffcc
        eeeeffcfccffffffcfffffffffffcccffeeeeefffffffcffffccfffffffffffffccffffceefcffffffffffffffffcccffffcceeeccccccccccffffffffffffccfccffffffffffcffffffffffffffffcf
        eeeeccfeecffffffccffffffffffffccfeeeeecffffffffcfccffffffcffffffccccfccceeccccffcccffffffcffcccfccfccccccccccccccccfccfccfccfffcceefffffffffffffffffffffffffffcf
        eeeecffeeffffcffffffffffffffffccfffcecfffffffcccffffffffffffffffffccfccccccccccfccccffffffffffffffffffffffcccccccccfccceeeeccffffcecffffffffffffccccccccfffffffc
        eeeeffeeeffffffffffffffffffffccfffffffffffffffffffffffffffffffffffffcccffcccfccfccccfcfffffffffffffffffffffffccccfffcccfcffcffffffccccffffffffffccceeeeeefffffcc
        ceefffcecfffffffffffffffffffffffffffffffffffffffffffffffccfccfffffffffffffffffccfcfffffffffffffffffffffffffffffffffffffffffffffffcffccfffffffffffffcceeeeecfcfcc
        fffffffccccffffffffffffffffffffffffffffffffffffffffffffccccccccccccffffffffffffffffcffffffffffffffffffcfffcffffffffffffffffffffffcfffcccfffffffffffffffceececfcf
        ffffffffffccffffffffcccccfffffffffffffffffffffccccccccfcccccccccffffffffffffffffffffffffffffffffffffcfcfcccfffffffffffffffffffffffffffffffffffffffccfffccfeffccf
        fffffffffffffcccccccccccfffffffffffffffffffccccccccccccccccccccccfffffffffffffffffffcffffffffffffffffccccccfffffffffffffffffffffffffffffffffffffffcecffceeefcfff
        ffffffffffffcccccccccccccccccfffffffffccffcccccccccccccccccccccccccfffffffffffffffffcfffffffffffffffcffcccfffffffffffffffffffffffffffffffffffffffffeeeeeeeeeeeff
        ccccccccccccccccecccccccbccccfffccccffcccccccccccccccccccccccccccccfffffffffffffffffffffffffffffffffccfffffffffffffffffffffcffffffffffffffffffffffceeeeeeeeeeecf
        cccccccccccccccceeccccccccccccccccccffccbbccccccccccccccccccccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffccecfeeeeeeeff
        ccccccccccccccfceeeccccccccccccccccccfcccccccccccccccccccccccccccffffffffffffffffffffffffffffffffffffffffffffccffffffffffffffcffffffffffffffffffffffcccfeeeeefff
        cccccccccccccfcfceccccccccccccccccccccccccccccccccecccccccccccccccccfffffffffffffffffffffffffcfffffffffcffffccccccccccccfffffffffffffffffccfcfffffffffffceefffff
        cccccccccccfccffccfcccccccccccccccccccccccccceeeccecccccccccccccccccccccccccccccccccccccccccccccccccffccfffccccccccccccccccfccccccfffffccccccffffffffffffcffcffc
        cccccccccccffcfffffcccccccccccccccccccbbbcccceeeeeeeccccccccccccccccccccccccccccccccccccccccccccccccccccccccfcccccccccccccccccccccccccfcfffcffffffffffffffffffcf
        cccccccccccccfcccccccccccccccccccccccccbbcccceeeeeeeccceccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccffffffffffffffffffffffff
        ccccccccccccfffcccccccccccccccccccccccccccccceeeeeeeccceeeecccccccccccccccccccccccccccccccccccccccecccccccccccccccccccccccccccccccccccccfffffccfffffffffffffffff
        ccccccccccccccccccccccccccccccccccccccccccccceeeeeecccfeeeeeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccfffccccccccccccccccccccffffffffffcff
        cccccccccccccccccccccccccccccccccccccccccccceeeeeeeccffceeeeeebbbbbbbbcccccccccccccccccccccccceccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccffeeccccfeeeeeebbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbecccccccebbbccccccbcccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccbcccfffceecffceeeeeeccebbbbbbbbbbbbbbbbbbbbbcccccccebeecbeeeeebbbbbbbcccbbbbbbcccccccccccccccccccbbbccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccffffffeefffcffeeeeccbbbbbccccbbbbeebbeeebcccccccccccccceeebbeebbbbbbbebbbbebbbccccccccccccccbbbbbbbbbbbbbbbbccbbbbc
        cccccccccccccccccccccccccccccccccccccccbbbbccfffffceecfffffceeeccbbcbbbbcccceeeeeeeeeccccbcceeecccccceeeeeeeeecebbebbbbbbbeccbccccccccccbbbbbbbbbbbbbbbbbebbcccc
        cccccccccccccccfcccccccccccccccccccccccccccccfffffcffffffffffffccccccccccccccceeecffeeccebeeebeeeccccceebeeccccceeeeebbbbbbbbbbbbbbbbcccceeeebbeebbebbbbbccccccc
        cccccccccccccccfcccccccccccccccccccccccccccccffffffffffffffffcfffcccccccccccccffffffeecceeeebbbbeeeccceeeeeccccbeeeeeeebbbbcbbbbbbbbbbbbeebeeeeeeeeebebccbbbcccc
        cccccccccccccccfccccccccccccccccccccccccccccffffffffffffffffffffcccccbbcccccccffffffcfffeeeeebbbeeeecceeeeccccceeeeeeeebbbeecceeeeebbbecbbbbbbeeeeeeeeebbbebeeee
        cccccffccccecccccccccccccccccccccccccccccccffffffffffffffffffffccccccccccccfccffffffcffffceeeeeceeeeeeeeeccccceeeeeeeeeeeeeebbeeeeeebeeeeeeeeeeeeeeeebbbbbccceee
        bccccffccceecccccccccccccccccccccccccccccfffffffffffffffffffffffcfccccccfcffccffffffffcffcfceccccceeeecccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebebbcccceee
        bcccfcfccceeccfccccccccccccccccccccccccccfffffffffffffffffffffffcfffcccfffffffffffffffffcffcccccccceeccccccceeeeecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccce
        cccccfffccccfffcccccccccccccccccccccfccccfffffffffffffffffffffffffffcccffffffffffffffffffffffccfffceecccccccceeecccceeecccceeeeeeeeeeeeeeeeeeeeeeeeeecccccccccee
        cccccfffffffffccccccccffccccccccccffffffffffffffffffffffffffffffffcfffcfffffffffffffffffffffffffffccecfccfcccccccffcccccffcceeccceeecccffceeeeeeeeeeccccccccccee
        """))
    effects.star_field.start_screen_effect()
    tioVilaStoryImg = img("""
        ......................................................eeeeeeee................................
        .....................................................eeeeeeeeee...............................
        ..................................................eeeeeeeeeeeeeee.............................
        ................................................eeeeeeeeeeeeeeeeeee...........................
        ...............................................eeeeeeeeeeeeeeeeeeeee..........................
        .............................................ceeeeeeeeeeeeeeeeeeeeeee.........................
        ............................................eeeeeeeeeeeeeeeeeeeeeeeeed........................
        ...........................................eeeeeeeeeeeeeeeeeeeeeeeeeeed.......................
        ...........................................eeeeeeeeeeeeeeeeeeeeeeeeeeee.......................
        ..........................................eeeeeeeeeeeeeeeeeeeeeeeeeeeeed......................
        ..........................................eeeeeeeeeeeeeeeeeeeeeeeeeeeeee......................
        ..........................................eeeeeeeeeeeeeeeeeeeeeeeeeeeeee......................
        ..........................................ceeeeeeeeeeeeeeeeeeeeeeeeeeeeee.....................
        ..........................................beeeeeeeeeeeeeeeeeeeeeeeeeeeeee.....................
        .........................................bbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee....................
        ..........................................ceeeebeeeeeeeeeeeeeeeeeeeeeeeeee....................
        ..........................................dddccbeeeeeeeeeeeeeeeeeeeeeeeeee....................
        .........................................bcddcddddeeeeeeeeeeddeeeeeeeeeeee....................
        ..........................................cddcddddddddddddddddeeeeeddddeee....................
        .........................................ddddddffccdddddddddddcfcbdddddeee....................
        .........................................fddddddcfffddddddddcfcbdbddddddee....................
        .........................................fdddddddddccddddddccdddddddddddee....................
        .........................................fddddddddddcdddddddddddddddddddcc....................
        .........................................fdddddddddddddddddddddddddddddddd....................
        .........................................fdddddddddddddddddddddddddddddddd....................
        ........................................bcddddcccccddddddddddccccddddddddd....................
        .......................................ffcddddccbbcfddddddddccbbccdddddddd....................
        .......................................fdddddddfcccccddddddddccfcddddddddd....................
        .......................................fdddddddddddddddddddddddddddddddddd....................
        .......................................fddddddddddddddddddddddddddcdddddd.....................
        ........................................fddddddddddddddddddddddddcdddddd......................
        ........................................fddddddddddddddddddddddddddddddd......................
        .........................................fcddddddddddddddddddddddddddddd......................
        ..........................................cdddddddddcddddddddddddddddddd......................
        ..........................................cdddddddddcdddddddddddddddddd.......................
        ...........................................dddddddddddddddddddddddddddd.......................
        ...........................................ddddddddccdddddddddddddddddd.......................
        ...........................................dddddddddddddddddddddddddddd.......................
        ...........................................dddddddddddddddddddddddddddd.......................
        ...........................................dddddddddddddddddddddddddddd.......................
        ...........................................cddddddddddddddddddddddddddd.......................
        ............................................cdddddddddddccccccdddddddc........................
        ............................................cbdddddddbcccccccdddddddd.........................
        ............................................ccbddddddcfcdddddddddddbc.........................
        ..............................................bddddddddddddddddddddb..........................
        ..............................................ccddddddddcdcfddddddbc..........................
        ...............................................ccddddddfccddddddddc...........................
        .................................................ddddddddddddddddc............................
        ..................................................dddddddccddddddc............................
        ..................................................cbddddddddddddfcb...........................
        ...................................................cbddddddddddcdd............................
        ....................................................ccdddddddccffddc..........................
        .....................................................ccdddddcfccbddc..........................
        .....................................................bddddddcbbdddbc..........................
        .....................................................ddbccdddddddddcc.........................
        .fffffffdf..........................................cddddddddddddddd..........................
        .fbfdfbfddf.........................................ccddddddddddddddcdddddddd.fffffffff.ff....
        .f.dddffddf.ff.......................................cddddddddddddddddccdddddff1111111ffff....
        .fffddddddddd.........................ff............ccdddddddddddddddddddddddff1111111111f....
        ..ff.dddddddd........................f.f..........ffdddddddddddddddddddddddddff1111111111f....
        fffffdddddddddd.....................f11.fff.fffffffdddddddddddddddddddddddddfff11111111111f...
        fdddddddddddddd.....................f1111.fffddddddddddddddddddddddddddddddddff11111111111f...
        ffddddddddddddf11..................f11111ffdddddddddddddddddddddddddddcdddddfb111111111111ff..
        .ffffdddddddddf111fff.............ff111111fddddddddddddddcddddddddddddddddfffb1111111111111f..
        ...f.ddddddddf1111d1f.............f11111111cddddddddddddddddddddddddddddddf1111111111111111f..
        ....ddddddddff1111111f...........ff11111111cbddddddddddddddddddddddddddddff1111111111111111f..
        ...ffdddddddf111111111ff.........f1111111111fbdddcddddddddddddddddddddddff111111111111111111f.
        ....fffffdddf1111111111ff......f.f1111111111fbddddddddcdddddddddddddddddff1d1111111111111111f.
        ........ffdff11111111111fff....fff1111111111fffdddddddddcdddddddcdddddfff1d11111111111111111f.
        .........ff.1111111111111fff...fbf111111111111ffffdddddddccddddcbddddfff11111111111111111111f.
        ...........ff11111111111111ff..f11111111111111111bfffffddddddddddddccbf111d11111111111ff111ff.
        ...........ff1111111111111111fff1111111111111111111111fffddddddddddc1c1d11d111111111fffffffff.
        ..........f1111111111111111111f1111111111111111111111c1dfffdddddddd1111111111111111.ffffffff..
        ..........f111111111111111111111111111111111111111111111fbfffffddddcc11111111111111fffff......
        ..........f1111111111111111111111111111111111111111111111ff11dfffff1111111111111111f..........
        ..........f11111111111111111111111111111111111111111111111111111f111111111111111111f..........
        ..........f111111111111111111111111111111111111111111111111111111111111111111111111f..........
        ..........f111111111111111111111111111111111111111111111111111111111111111111111111bf.........
        .........ff111111111111111111111111111111111111111111111111111111111111111111111111.f.........
        .........f11111111111111111111111111111111111111111111111111111111111111111111111111f.........
        .........ff111111111111111111111111111111.f111111111111111111111111111111111111d11dff.........
        ..........fffffffffff1111111111111111111fff1111111111111111111111111111111111111d1ff..........
        .....................ff11ff111111111111ff.11111111111111111111111111111111111111fff...........
        ......................ffffffffff111111fff.111111111111111111111111111111111111fff.............
        ...............................ffffffff.ff111111111111111111111111111111111bbff...............
        .........................................ff11111111111111111111111111111bbbfff................
        ..........................................fffffff1111111111111111111111bfff...................
        .............................................bbbbfffff111111111111111ffffb....................
        ................................................bbbbbbffffffffffffffff........................
        .....................................................bbbbbbbbbbbf.............................
        """)
    tioVilaStorySprite = sprites.create(tioVilaStoryImg, 0)
    tioVilaStorySprite.set_position(105, 40)
    story.print_text("Despues de maldecir al tio vila la princesa desaparecio",
        80,
        100,
        15,
        1,
        story.TextSpeed.FAST)
    story.print_text("El tio vila volvió a su casa y de camino falleció con la lengua fuera",
        80,
        100,
        15,
        1,
        story.TextSpeed.FAST)
    tioVilaStorySprite.destroy()
    IrFase("final", "credits")
    pause(2000)
multigame.on_start("final", on_on_start5)

def on_on_start6():
    global CreditsCharacters, CreditsCharactersNames
    music.stop_all_sounds()
    scene.set_background_image(img("""
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """))
    music.play(music.create_song(hex("""
            00780004080200
            """)),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    CreditsCharacters = ["Arturo",
        "Santi",
        "Miguel",
        "Rim",
        "Hugo",
        "Ismael",
        "Sofia",
        "Keila",
        "Nerea",
        "Antonio",
        "Patricia"]
    CreditsCharactersNames = ["programador",
        "programador",
        "programador",
        "ilustradora",
        "ilustrador",
        "ilustrador",
        "escritora",
        "editora",
        "editora",
        "editor",
        "directora",
        ""]
    RoleCredits()
    game.reset()
multigame.on_start("credits", on_on_start6)

def EndGame():
    sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
arana: Sprite = None
pinguino: Sprite = None
serpiente: Sprite = None
vampiro: Sprite = None
calavera: Sprite = None
tiburon: Sprite = None
enemyRandom = 0
tioVilaStorySprite: Sprite = None
tioVilaStoryImg: Image = None
CreditsCharactersNames: List[str] = []
CharacterText: TextSprite = None
textSprite: TextSprite = None
CreditsCharacters: List[str] = []
creditsIndex = 0
encantaSprite: Sprite = None
tioVilaEndingSprite: Sprite = None
textSprite2: TextSprite = None
myMenu: miniMenu.MenuSprite = None
titleTextSprite: TextSprite = None
tempBackground: Image = None
tioVilaSprite: Sprite = None
velocidadScroll = 0
aceleracionSalto = 0
velocidadSalto = 0
reyStorySprite: Sprite = None
encantaStorySprite: Sprite = None
princesaStoryImg: Image = None
reyStoryImg: Image = None
fase = ""
pesadilla = False
initGame = False
InitMenuFase()

def on_update_interval3():
    global enemyRandom, tiburon, calavera, vampiro, serpiente, pinguino, arana, pesadilla
    if fase == "game":
        enemyRandom = randint(1, 6)
        if enemyRandom == 1:
            tiburon = sprites.create_projectile_from_side(img("""
                    .............ccfff..............
                    ...........ccddbcf..............
                    ..........ccddbbf...............
                    ..........fccbbcf...............
                    .....fffffccccccff.........ccc..
                    ...ffbbbbbbbcbbbbcfff....ccbbc..
                    ..fbbbbbbbbcbcbbbbcccff.cdbbc...
                    ffbbbbbbffbbcbcbbbcccccfcdbbf...
                    fbcbbb11ff1bcbbbbbcccccffbbf....
                    fbbb11111111bbbbbcccccccbbcf....
                    .fb11133cc11bbbbcccccccccccf....
                    ..fccc31c111bbbcccccbdbffbbcf...
                    ...fc13c111cbbbfcddddcc..fbbf...
                    ....fccc111fbdbbccdcc.....fbbf..
                    ........ccccfcdbbcc........fff..
                    .............fffff..............
                    """),
                randint(-70, -125.5),
                0)
            animation.run_image_animation(tiburon,
                assets.animation("""
                    enemy_tiburon
                    """),
                200,
                True)
            tiburon.set_position(160, 81)
        if enemyRandom == 2:
            calavera = sprites.create_projectile_from_side(img("""
                    ........................
                    ........................
                    ........................
                    ........................
                    .........fffff..........
                    ........f11111ff........
                    .......fb111111bf.......
                    .......f1111111dbf......
                    ......fd111111dddf......
                    ......fd11111ddddf......
                    ......fd11dddddddf......
                    ......f111dddddddf......
                    ......f11fcddddddf......
                    .....fb1111bdddbf.......
                    .....f1b1bdfcfff........
                    .....fbfbffffffff.......
                    ......fffffffffff.ff....
                    ...........ffffffff.....
                    ........f1b1bffffff.....
                    ........fbfbffffff......
                    ........................
                    ........................
                    ........................
                    ........................
                    """),
                randint(-70, -125.5),
                0)
            animation.run_image_animation(calavera,
                assets.animation("""
                    enemy_calavera
                    """),
                200,
                True)
            calavera.set_position(160, 88)
        if enemyRandom == 3:
            vampiro = sprites.create_projectile_from_side(assets.image("""
                    myImage2
                    """),
                randint(-100, -150),
                0)
            animation.run_image_animation(vampiro,
                assets.animation("""
                    enemy_vampiro
                    """),
                100,
                True)
            vampiro.set_position(160, 58)
        if enemyRandom == 4:
            serpiente = sprites.create_projectile_from_side(assets.image("""
                    myImage2
                    """),
                randint(-60, -120),
                0)
            animation.run_image_animation(serpiente,
                assets.animation("""
                    enemy_serpiente
                    """),
                200,
                True)
            serpiente.set_position(160, 88)
        if enemyRandom == 5:
            pinguino = sprites.create_projectile_from_side(assets.image("""
                    myImage2
                    """),
                randint(-60, -120),
                0)
            animation.run_image_animation(pinguino,
                assets.animation("""
                    enemy_pinguino
                    """),
                200,
                True)
            pinguino.set_position(165, 88)
        if enemyRandom == 6:
            arana = sprites.create_projectile_from_side(assets.image("""
                myImage2
                """), randint(-60, -80), 0)
            animation.run_image_animation(arana,
                assets.animation("""
                    enemy_spider
                    """),
                200,
                True)
            arana.set_position(160, 65)
    if info.score() >= 12 and not (pesadilla):
        pesadilla = True
        RandomizeImage(scene.background_image())
game.on_update_interval(randint(1000, 2000), on_update_interval3)
