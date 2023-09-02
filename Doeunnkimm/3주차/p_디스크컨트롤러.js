function solution(jobs) {
  const waitingRoom = []
  let currentTime = 0
  let totalTime = 0

  const scheduling = () => {
    if (!waitingRoom.length) return false

    const [inputTime, workTime] = waitingRoom.shift()
    totalTime += currentTime - inputTime + workTime
    currentTime += workTime
    return true
  }

  const insertJob = (job) => {
    waitingRoom.push(job)
    waitingRoom.sort((a, b) => a[1] - b[1]) // 작업 시간이 짧은 것부터 수행되기 위해
  }

  jobs
    .sort((a, b) => a[0] - b[0])
    .forEach(([inputTime, workTime]) => {
      // 현재 시간 < 요청 시점이라면 => 작업 없이 흘러가야 하는 시간
      while (currentTime < inputTime) {
        // 대기 중인 작업도 없다면
        if (!scheduling()) {
          currentTime = inputTime
        }
      }
      insertJob([inputTime, workTime]) // wait 시키기
    })

  while (waitingRoom.length > 0) {
    scheduling()
  }

  return parseInt(totalTime / jobs.length)
}
