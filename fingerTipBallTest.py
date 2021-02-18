import pybullet as p
import time
import pybullet_data
import pybulletX as px


def main():
    px.init()

    startPos = [0, 0, 0]
    startOrientation = p.getQuaternionFromEuler([0, 0, 0])
    boxId = p.loadURDF("resources/fingerTip.urdf", startPos, startOrientation)

    while True:
        time.sleep(0.01)
        p.stepSimulation()


if __name__ == "__main__":
    main()
