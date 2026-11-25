# erasers_g1_description

|**ROS2**|**Mujoco**|
|:---:|:---:|
|<img src="https://i.imgur.com/bjOdG4P.png"/>|<img src="https://i.imgur.com/FgVuLP3.png"/>|

　Unitree G1 のロボットモデル（URDF，MJCF）を提供するリポジトリです．

　ROS2 ワークスペースまたは任意のディレクトリにこのリポジトリをクローンします．
```bash
git clone git@github.com:trcp/erasers_g1_description.git
```

## セットアップ手順（ROS2）

1. `rosdep ` を用いてリポジトリの依存関係をインストールします．
    - GUI ツール群を含める場合<br>
        　RViz2 などのビジュアライズツールの依存関係を追加する場合．
        ```bash
        rosdep update --rosdistro $ROS_DISTRO &&\
        rosdep install -y -i --from-path src/erasers_g1_description
        ```    
    - GUI ツールを含めない場合<br>
       　 Rviz2 などのビジュアライズツールを含めない場合．
       ```bash
       rosdep update --rosdistro $ROS_DISTRO &&\
       rosdep install -y -i --from-path src/erasers_g1_description \
            --skip-keys rviz2 \
            --skip-keys joint_state_publisher_gui
       ```
1. ワークスペース上でパッケージをビルドします．
    ```bash
    colcon build --symlink-install --packages-select erasers_g1_description
    ```
1. ビジュアライズツールで Unitree G1 を視覚化する場合．
    >>>[!note]
    デフォルトのロボットモデルは [erasers_g1](urdf/erasers_g1.urdf) です．ロボットモデルの変更は `robot_model` 引数を指定してください．詳細は以下のコマンドを実施してください．
    ```bash
    ros2 launch erasers_g1_description display.launch.py --show-args
    ```
    >>>
    ```bash
    ros2 launch erasers_g1_description display.launch.py use_rviz:=true
    ```
    |**erasers_g1**|**g1_23dof**|**g1_29dof**|
    |:---:|:---:|:---:|
    |<img src="https://i.imgur.com/bjOdG4P.png"/>|<img src="https://i.imgur.com/QXvZ3Q5.png"/>|<img src="https://i.imgur.com/kvnqP74.png"/>|

## セットアップ手順（Mujoco）

　以下のコマンドでロボットのビジュアライズが可能です．
```bash
python -m mujoco.viewer --mjcf mjcf/g1_23.mjcf
```
