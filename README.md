# erasers_g1_description

Unitree G1（23-DOF および 29-DOF）の ROS 2 向け URDF（$`\text{Unified Robot Description Format}`$）および MuJoCo 向け MJCF（$`\text{MuJoCo XML Modeling Format}`$）記述パッケージです．

## モデル構成

- `mjcf/g1_23dof.xml` : Unitree G1 23 自由度モデル用 MJCF
- `mjcf/g1_29dof.xml` : Unitree G1 29 自由度モデル用 MJCF
- `urdf/g1_23dof.urdf` : Unitree G1 23 自由度モデル用 URDF
- `urdf/g1_29dof.urdf` : Unitree G1 29 自由度モデル用 URDF
- `meshes/*.STL` : 両モデルで参照される 3D メッシュ一式

## セットアップ手順（ROS 2）

1. **依存関係のインストール**<br>
   ワークスペースの `src/` 配下に本リポジトリを配置した状態で，必要な ROS 2 パッケージを導入します．
   ```bash
   rosdep update --ros-distro $ROS_DISTRO && \
   rosdep install -y -i --from-path src/erasers_g1_description
   ```

1. **パッケージのビルド**<br>
   ワークスペースルートで `colcon build` を実行します．
   ```bash
   colcon build --symlink-install --packages-select erasers_g1_description
   ```

1. **RViz2 による可視化確認**<br>
   引数 `robot_model` に `g1_23dof` または `g1_29dof` を指定して起動できます．
   ```bash
   ros2 launch erasers_g1_description display.launch.py use_rviz:=true robot_model:=g1_23dof
   ```

## セットアップ手順（MuJoCo）

1. **MuJoCo ビューアでの単体確認**<br>
   以下のコマンドで `g1_23dof` または `g1_29dof` の MJCF モデルを直接確認できます．
   ```bash
   python -m mujoco.viewer --mjcf mjcf/g1_23dof.xml
   ```
