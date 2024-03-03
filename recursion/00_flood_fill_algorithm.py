# https://www.geeksforgeeks.org/problems/flood-fill-algorithm1856/1

# Input:
# 1 1 1
# 1 1 0
# 1 0 1

# Ans:
# 2 2 2
# 2 2 0
# 2 0 1


def helper(self, image, i, j, oc, nc):
    n = len(image)
    m = len(image[0])

    if not 0 <= i < n or not 0 <= j < m or image[i][j] != oc or image[i][j] == nc:
        return image

    image[i][j] = nc

    self.helper(image, i, j + 1, oc, nc)
    self.helper(image, i, j - 1, oc, nc)
    self.helper(image, i + 1, j, oc, nc)
    self.helper(image, i - 1, j, oc, nc)

    return image


def floodFill(self, image, sr, sc, newColor):

    ans = self.helper(image, sr, sc, image[sr][sc], newColor)
    return ans


if __name__ == "__main__":
    image = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}}
    ans = floodFill(image, 1, 1, 2)
    print(ans)
