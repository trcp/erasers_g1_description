# erasers_g1_description

[English](README.md) | **日本語**

|**ROS 2**|**MuJoCo**|
|:---:|:---:|
|<img src="https://i.imgur.com/bjOdG4P.png"/>|<img src="https://i.imgur.com/diU8Yxh.png"/>|

Unitree G1 のロボットモデル（URDF，MJCF）を提供するリポジトリです．

ROS 2 ワークスペースまたは任意のディレクトリに本リポジトリをクローンします．

```bash
git clone git@github.com:trcp/erasers_g1_description.git
```

## セットアップ手順（ROS 2） <a id="setup-ros2"></a>

1. **依存関係のインストール**<br>
   `rosdep` を用いてリポジトリの依存関係をインストールします．
   - GUI ツール群を含める場合（RViz 2 などのビジュアライズツールの依存関係を追加する場合）：
     ```bash
     rosdep update --rosdistro $ROS_DISTRO && \
     rosdep install -y -i --from-path src/erasers_g1_description
     ```
   - GUI ツールを含めない場合（RViz 2 などのビジュアライズツールを含めない場合）：
     ```bash
     rosdep update --rosdistro $ROS_DISTRO && \
     rosdep install -y -i --from-path src/erasers_g1_description \
         --skip-keys rviz2 \
         --skip-keys joint_state_publisher_gui
     ```
1. **パッケージのビルド**<br>
   ワークスペース上でパッケージをビルドします．
   ```bash
   colcon build --symlink-install --packages-select erasers_g1_description
   ```
1. **ロボットモデルの表示**<br>
   ビジュアライズツールで Unitree G1 を視覚化します．
   ```bash
   ros2 launch erasers_g1_description display.launch.py use_rviz:=true
   ```

   |**erasers_g1**|**g1_23dof**|**g1_29dof**|
   |:---:|:---:|:---:|
   |<img src="https://i.imgur.com/bjOdG4P.png"/>|<img src="https://i.imgur.com/QXvZ3Q5.png"/>|<img src="https://i.imgur.com/kvnqP74.png"/>|

> [!NOTE]
> デフォルトのロボットモデルは [erasers_g1](urdf/erasers_g1.urdf) です．ロボットモデルを変更する場合は `robot_model` 引数を指定してください．詳細は以下のコマンドを実行して確認してください．
> ```bash
> ros2 launch erasers_g1_description display.launch.py --show-args
> ```

## セットアップ手順（MuJoCo） <a id="setup-mujoco"></a>

以下のコマンドでロボットモデルのビジュアライズが可能です．

```bash
python -m mujoco.viewer --mjcf mjcf/g1_23.mjcf
```
