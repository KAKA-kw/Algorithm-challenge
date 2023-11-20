const readline = require('readline')
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const input = []
rl.on('line', function (line) {
  input.push(line)
}).on('close', function () {
  const arr = input.slice(1).map((xyn) => xyn.split(' ').map(Number))

  arr.forEach((xyn) => {
    const [x, y, n] = xyn

    // x, y 좌표를 통해 총 이동거리 계산
    // (0, -5) => 결국 0 + 5 => 5칸 이동 필요
    const sum = Math.abs(x) + Math.abs(y)

    // 정답을 담을 변수를 선언하고 초기값을 NO로 설정
    let answer = 'NO'

    // 총 이동거리가 n보다 작거나 같고
    // 총 이동거리와 n의 차이가 짝수라면 YES를 출력한다.
    // (남은 시간이 짝수여야 같은 곳을 방문해서라도 정답에 도달할 수 있다.)
    if (sum <= n && (n - sum) % 2 === 0) answer = 'YES'

    console.log(answer)
  })
})
