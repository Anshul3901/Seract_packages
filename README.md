# 🤖 SO-100 Arm – Grabbing Position Command

Use the following command to move the SO-100 Arm to its **grabbing position**:

```bash
ros2 action send_goal /so_100_arm_controller/follow_joint_trajectory \
  control_msgs/action/FollowJointTrajectory \
  "{trajectory: {
     joint_names: ['Shoulder_Rotation','Shoulder_Pitch','Elbow','Wrist_Pitch','Wrist_Roll'],
     points: [{positions: [0.0, 1.3, -0.3, 0.0, 0.0], time_from_start: {sec: 2}}]
   }}"
