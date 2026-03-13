# Unitree Go2 pour la cartographie 

## Activation de l'environement viruelle afin de controler le robot 

```bash
. go2_ws/install/setup.bash
source /opt/ros/humble/setup.bash
source ~/go2_ws/install/setup.bash
```

## Pour recompiler tout le projet 
```bash
cd <your_ws>    <==> cd /home/pierre/go2_ws/src/unitree-go2-ros2

colcon build 
source install/setup.bash

```
## Voir les processuss encours d'excecution 
```bash
ps aux | grep gazebo
```
## Pour arreter les processus encours
```bash
killall gzserver gzclient 
killall -9 gzserver
killall -9 gzclient
killall -9 gazebo

```

## Afficher les mondes disponibles dans Gazebo
```bash
ls /usr/share/gazebo-11/worlds
```
## Pour explorer avec le robot les differents mondes fournit par gazebo
### Phase 1 : ouvrir le world avec le robot à l'interieur 
Rviz = true permet dactiver la vue du robot et est optionnel

```bash
ros2 launch go2_config gazebo_custom_world.launch.py \
world:=/usr/share/gazebo-11/worlds/cafe.world rviz:=true

```

### Phase 2 : controler les mouvements du robot
#### methode 1 : 
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=/cmd_vel
```
| Touche | Action                              |
| ------ | ----------------------------------- |
| `i`    | Avancer (axe X positif)             |
| `k`    | Reculer (axe X négatif)             |
| `j`    | Tourner à gauche (axe Z positif)    |
| `l`    | Tourner à droite (axe Z négatif)    |
| `u`    | Avancer en diagonale avant-gauche   |
| `o`    | Avancer en diagonale avant-droite   |
| `m`    | Reculer en diagonale arrière-gauche |
| `,`    | Reculer en diagonale arrière-droite |
| `.`    | Stop / arrêt                        |
------------------------------------------------
#### methode 2 : donne le mouvement à effectuer dans la commande 
```bash
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist \
"{linear: {x: 0.5, y: 0.0, z: 0.0}, angular: {z: -0.5}}"

pour l arreter 
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist \
"{linear: {x: 0.0}, angular: {z: 0.0}}"
```
Explication

linear.x = 0.5 → avancer

linear.x = -0.5 → reculer

angular.z = 0.5 → tourner à gauche

angular.z = -0.5 → tourner à droite

ros2 topic pub /cmd_vel geometry_msgs/msg/Twist \
"{linear: {x: 0.0}, angular: {z: 0.5}}"


## Lancer le robot dans un environment avec le lidar activer 
### Phase 1 : Terminal 1 : Lancer Gazebo + Go2 dans le café world   colcon build --symlink-install
Activer l'environement
```bash
ros2 launch go2_config gazebo_custom_world_velodyne.launch.py world:=/usr/share/gazebo-11/worlds/cafe.world  rviz:=true
```
### Phase 2 : Terminal 2 : Lancer le teleop afin de controler les mouvements du robot

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=/cmd_vel
```

### Phase 3 : optionnel voir les ordres de mouvement que le robot reçoit 
```bash
ros2 topic echo /cmd_vel
```

