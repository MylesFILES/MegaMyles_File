let Player = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(Player)
tiles.setTilemap(tilemap`level1`)
scene.cameraFollowSprite(Player)
