FROM ros:jazzy-ros-base

SHELL [ "/bin/bash", "-c" ]

WORKDIR /

RUN source /opt/ros/jazzy/setup.bash

WORKDIR /ros2_ws

COPY ./simple_publisher_pkg /ros2_ws/src/simple_publisher_pkg

RUN colcon build --symlink-install

RUN source install/setup.bash

# CMD ["bash", "-c", "cd ..", "source /opt/ros/jazzy/setup.bash", "cd ros2_ws/", "source install/setup.bash && ros2 launch simple_publisher_pkg simple_publisher.launch.py"]

CMD ["bash", "-c", "source install/setup.bash && ros2 launch simple_publisher_pkg simple_publisher.launch.py"]