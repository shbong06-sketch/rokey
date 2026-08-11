FROM ros:jazzy-ros-base
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-colcon-common-extensions \
    ros-jazzy-rosidl-default-generators \
    python3-psycopg2 \
    python3-dotenv && \
    rm -rf /var/lib/apt/lists/*

COPY ./src/mission_worker_pkg ./src/mission_worker_pkg
COPY ./src/doosan-robot2/dsr_msgs2 ./src/doosan-robot2/dsr_msgs2

RUN . /opt/ros/jazzy/setup.sh && \
    colcon build --packages-select dsr_msgs2

CMD ["bash", "-c", ". /opt/ros/jazzy/setup.sh && . /app/install/setup.sh && exec python3 src/mission_worker_pkg/mission_worker_pkg/mission_worker.py"]