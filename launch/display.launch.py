from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import LogInfo
from launch.conditions import IfCondition
from launch.substitutions import Command
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    ld = LaunchDescription()


    # default variables
    pkg_share_dir = get_package_share_directory('erasers_g1_description')
    default_rviz_config_path = os.path.join(pkg_share_dir, 'rviz', 'g1.rviz')
    default_urdf_dir_prefix = os.path.join(pkg_share_dir, 'urdf') + os.sep
    default_robot_model = 'g1_23dof'


    # launch configurations
    robot_model = LaunchConfiguration('robot_model')
    use_rviz = LaunchConfiguration('use_rviz')


    # launch arguments
    declare_robot_model = DeclareLaunchArgument(
        'robot_model',
        default_value=default_robot_model,
        description='Unitree G1 model variant to display (g1_23dof or g1_29dof).'
    )
    declare_use_rviz = DeclareLaunchArgument(
        'use_rviz',
        default_value='false',
        description='Whether to start RViz2 and joint_state_publisher_gui.'
    )
    ld.add_action(declare_robot_model)
    ld.add_action(declare_use_rviz)


    # actions
    log_launch_action = LogInfo(msg=['Launching erasers_g1_description for model: ', robot_model])
    ld.add_action(log_launch_action)


    # nodes
    robot_description_content = ParameterValue(
        Command(['xacro ', default_urdf_dir_prefix, robot_model, '.urdf']),
        value_type=str,
    )
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        emulate_tty=True,
        output='screen',
        parameters=[{'robot_description': robot_description_content}],
    )
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        emulate_tty=True,
        output='screen',
        condition=IfCondition(use_rviz),
    )
    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', default_rviz_config_path],
        emulate_tty=True,
        output='screen',
        condition=IfCondition(use_rviz),
    )
    ld.add_action(robot_state_publisher_node)
    ld.add_action(joint_state_publisher_gui_node)
    ld.add_action(rviz2_node)


    return ld
