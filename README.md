# erasers_g1_description

**English** | [日本語](README_ja.md)

|**ROS 2**|**MuJoCo**|
|:---:|:---:|
|<img src="https://i.imgur.com/bjOdG4P.png"/>|<img src="https://i.imgur.com/FgVuLP3.png"/>|

A repository providing robot models (URDF and MJCF) for the Unitree G1 humanoid robot.

Clone this repository into your ROS 2 workspace or any preferred directory:

```bash
git clone git@github.com:trcp/erasers_g1_description.git
```

## Setup Instructions (ROS 2) <a id="setup-instructions-ros-2"></a>

1. **Install Dependencies**<br>
   Install dependencies for the repository using `rosdep`:
   - When including GUI tools (e.g., visualization tools such as RViz 2):
     ```bash
     rosdep update --rosdistro $ROS_DISTRO && \
     rosdep install -y -i --from-path src/erasers_g1_description
     ```
   - When excluding GUI tools:
     ```bash
     rosdep update --rosdistro $ROS_DISTRO && \
     rosdep install -y -i --from-path src/erasers_g1_description \
         --skip-keys rviz2 \
         --skip-keys joint_state_publisher_gui
     ```
1. **Build Package**<br>
   Build the package in your workspace:
   ```bash
   colcon build --symlink-install --packages-select erasers_g1_description
   ```
1. **Visualize Robot Model**<br>
   Visualize the Unitree G1 using visualization tools:
   ```bash
   ros2 launch erasers_g1_description display.launch.py use_rviz:=true
   ```

   |**erasers_g1**|**g1_23dof**|**g1_29dof**|
   |:---:|:---:|:---:|
   |<img src="https://i.imgur.com/bjOdG4P.png"/>|<img src="https://i.imgur.com/QXvZ3Q5.png"/>|<img src="https://i.imgur.com/kvnqP74.png"/>|

> [!NOTE]
> The default robot model is [erasers_g1](urdf/erasers_g1.urdf). To change the robot model, specify the `robot_model` argument. For more details, run the following command:
> ```bash
> ros2 launch erasers_g1_description display.launch.py --show-args
> ```

## Setup Instructions (MuJoCo) <a id="setup-instructions-mujoco"></a>

You can visualize the robot using the following command:

```bash
python -m mujoco.viewer --mjcf mjcf/g1_23.mjcf
```
