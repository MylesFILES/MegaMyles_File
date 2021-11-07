Player = sprites.create(img("""
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
            f f f f f f f 7 7 f f f f f f f 
            f f f f f f f 7 7 f f f f f f f 
            f f f f f f f 7 7 f f f f f f f 
            f f f f f f f 7 7 f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            7 7 7 7 7 7 f f f f 7 7 7 7 7 7 
            7 7 7 7 7 7 f f f f 7 7 7 7 7 7 
            7 7 7 7 7 7 f f f f 7 7 7 7 7 7 
            7 7 7 7 7 7 f f f f 7 7 7 7 7 7 
            7 7 7 7 7 7 f f f f 7 7 7 7 7 7 
            7 7 7 7 7 7 f f f f 7 7 7 7 7 7 
            7 7 7 7 7 7 f f f f 7 7 7 7 7 7 
            7 7 7 7 7 7 f f f f 7 7 7 7 7 7 
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    """),
    SpriteKind.player)
controller.move_sprite(Player)
tiles.set_tilemap(tilemap("""
    level1
"""))
scene.camera_follow_sprite(Player)