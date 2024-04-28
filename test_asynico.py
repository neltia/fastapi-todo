# asyncio 라이브러리 호출: 비동기 프로그래밍을 위한 파이썬 표준 라이브러리
import asyncio
import datetime


# 비동기적으로 실행될 함수를 정의, 'async def'를 사용해 정의
async def task(seconds):
    # 시작 메시지 출력, 작업 종료 시간 확인
    print(f'[작업시작] {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print(f"이 작업은 {seconds} 초 뒤 종료됩니다.")

    # asyncio.sleep 함수를 사용하여 비동기적으로 지정된 시간 동안 대기
    # 'await'는 이 함수가 완료될 때까지 현재 코루틴의 실행 일시 중지
    await asyncio.sleep(seconds)

    # 작업 완료 메시지 출력
    print("작업이 끝났습니다.")
    print(f'[작업종료] {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


# 메인 함수 정의
async def main():
    # asyncio.gather를 사용하여 여러 코루틴(task 함수 호출)을 동시에 실행
    # 이렇게 하면 task(1), task(2), task(3)이 거의 동시에 시작
    await asyncio.gather(
        task(1),
        task(2),
        task(3)
    )

# 프로그램의 시작점
# asyncio.run을 사용하여 메인 함수를 실행
# 이벤트 루프를 시작하고 main 코루틴 실행
print(main())
asyncio.run(main())
