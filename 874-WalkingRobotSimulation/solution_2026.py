import numpy as np

class Solution:

    # Another way to handle rotate is to have all facing in a list and
    # then use a pointer to move left or right, and use mod after move
    left_rotate_mat = np.array([[0, -1], [1, 0]])
    right_rotate_mat = left_rotate_mat @ left_rotate_mat @ left_rotate_mat
    # right_rotate_mat = np.array([[0, 1], [-1, 0]])

    def move(self, pos, facing, command, obs):
        match command:
            case -2:
                return pos, self.left_rotate_mat @ facing
            case -1:
                return pos, self.right_rotate_mat @ facing
            case _:
                for _ in range(command):
                    new_pos = pos + facing
                    if (new_pos[0] in obs) and (new_pos[1] in obs[new_pos[0]]):
                        return pos, facing
                    else:
                        pos = new_pos
                return pos, facing

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # construct obs map
        obs = {}
        for x, y in obstacles:
            if x not in obs: obs[x] = set()
            obs[x].add(y)

        # move and update
        res = np.int64(0)
        pos = np.array((0, 0))
        facing = np.array((0, 1))

        for c in commands:
            pos, facing = self.move(pos, facing, c, obs)
            res = max(res, pos @ pos.T)

        return res.item()
