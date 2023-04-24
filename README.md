# 중대형 디스플레이를 위한 시선추적 프로그램 (nemoGaze)
## 스타랩 6차년도 과제
NEMOSHELL 플랫폼은 중대형 디스플레이 기기에서 다중 사용자 환경을 제공하지만 사용자가 어떤 어플리케이션을 주로 사용하는 지 알 수 있는 기술은 제공하지 않는다. NEMOSHELL 플랫폼의 다중 사용자 환경은 중대형 디스플레이 기기에서 동작하는 만큼 여러 어플리케이션이 동시에 사용된다는 특성을 가진다. 각 어플리케이션마다 하드웨어 자원이 할당되고 어플리케이션의 수가 늘어남에 따라 하드웨어 자원 경쟁으로 인해 어플리케이션 간 성능 간섭으로 성능 저하가 야기될 수 있다. 따라서 하드웨어 자원을 어플리케이션들에게 효율적으로 분배시켜줄 수 있어야한다. 즉, 다중 사용자 환경에서 어떤 어플리케이션이 많은 사용자들에게 사용 중인지 확인할 수 있어야 한다. 따라서 본 프로젝트에서는 NEMOSHELL 플랫폼에서 사람들의 시선을 판별하여 실시간으로 다중 사용자가 주목하고 있는 Foreground Application을 판단할 수 있도록 nemoGaze를 개발하였다.
nemoGaze의 목적은 사람들이 현재 화면의 어디에 집중하고 있는지 확인해 Foreground Application을 확인하는 것이므로 웹캠을 사용해 실시간으로 이미지를 받아 처리한다. 이를 위해 본 프로젝트는 OpenCV 기술을 기반으로 개발된 Gaze Tracking 오픈소스를 사용하여 개발되었으며 이를 통해 다중 사용자의 시선을 판별해 현재 실행 중인 Application 중 Foreground Application을 확인할 수 있다. nemoGaze는 받아온 이미지를 통해 사람들의 눈 및 동공의 위치를 확인하고 방향을 계산해 사람들이 보고 있는 위치를 중대형 디스프레이에 표시하여 Foregorund Application을 알 수 있다. 

기반 기술 출처: https://github.com/antoinelame/GazeTracking

### 사용 환경
- NEMOSHELL 플랫폼에서 동작
- 우분투 환경에서 동작
- GazeTracking API 사용
- 파이썬3 환경에서 동작

### 실행 방법
1. sudo apt-get install cmake
2. sudo apt-get install libboost-all-dev
3. pip3 install -r requirements.txt
4. python3 gaze_tracking.py

## Sources Used
* [Gaze Tracking](https://github.com/antoinelame/GazeTracking) MIT License


*이 기술은 SW스타랩으로부터 지원받았음*
