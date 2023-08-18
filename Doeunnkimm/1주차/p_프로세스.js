function solution(priorities, location) {
  const copyPriorities = [...priorities]
  const dataset = priorities.map((priority, idx) => ({priority, idx}))
  let count = 0

  while (dataset.length !== 0) {
    const maxValue = Math.max(...copyPriorities)
    const {priority, idx} = dataset.shift()
    if (priority >= maxValue) {
      count++
      copyPriorities[idx] = -1
      if (idx === location) {
        break
      }
    } else {
      dataset.push({priority, idx})
    }
  }
  return count
}
