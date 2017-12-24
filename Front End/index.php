<!DOCTYPE html>
<html>
    <head>
        <title>Garage Door Opener</title>
    </head> 
    <body>
        <div>
            <form method="post">
                <input class="door" type="submit" name="door" id="door_button" value="Garage Door" onclick="<?php garageDoor();?>" />
            </form> 
        </div>
        <style>
            .door {
                background-color: gray;
                height: 100px;
                width: 50%;
                font-size: 60px;
                top: 50%;
                margin: auto;
                display: block;
            }
        </style>
        <?php
            function garageDoor() {
                if (isset($_POST['door'])) {
                    exec('sudo python /home/pi/GarageDoorApp/Python/garage_door.py');
                }
            }
        ?>
    </body>
</html>