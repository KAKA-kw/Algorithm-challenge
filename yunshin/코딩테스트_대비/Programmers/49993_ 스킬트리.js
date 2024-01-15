const solution = (skill, skill_trees) => {
  const possible = skill_trees.map((skill_tree, idx) => {
    const stack = []
    let flag = true
    skill_tree.split('').forEach((learned) => {
      if (skill.includes(learned)) {
        if (skill[stack.length] == learned) stack.push(learned)
        else flag = false
      }
    })
    return flag
  })
  return possible.filter((isPossible) => isPossible).length
}
