function solution(bridge_length, weight, truck_weights) {
  let time = 0
  let bridge_on_truck = Array.from({length: bridge_length}, () => 0)
  let weights_sum = 0

  // 맨 앞 트럭 이동
  time++
  bridge_on_truck.shift()
  weights_sum += truck_weights[0]
  bridge_on_truck.push(truck_weights.shift())

  // 다리 위애 올라간 트럭이 존재한다면
  while (weights_sum > 0) {
    // 다리 위에 있는 맨 앞 트럭 -> 다리를 나감
    time++
    weights_sum -= bridge_on_truck.shift() // 배열에서 빼면서 sum에서도 빼게 된다

    // 대기 트럭이 남아 있는데, 그 다음 트럭이 올라왔을 때 버틸 수 있는 무게라면
    if (truck_weights.length > 0 && weights_sum + truck_weights[0] <= weight) {
      weights_sum += truck_weights[0]
      bridge_on_truck.push(truck_weights.shift())
    } else {
      bridge_on_truck.push(0)
    }
  }
  return time
}
