from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="controller_manager",
            executable="ros2_control_node",
            parameters=[
                {"robot_description": open("/home/gixadmin/so-arm_ws/install/so_100_arm/share/so_100_arm/config/so_100_arm.urdf.xacro").read()},
                "/home/gixadmin/so-arm_ws/install/so_100_arm/share/so_100_arm/config/ros2_controllers.yaml",
            ],
            output="screen",
        ),
        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["so_100_arm_controller"],
            output="screen",
        ),
        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["so_100_gripper_controller"],
            output="screen",
        ),
    ])
