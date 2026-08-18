class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flip_image = []
        for row in image:
            flip_image.append(row[::-1])
        
        inverted_image = []
        for row in flip_image:
            inverted_image.append([1 - x for x in row])

        return inverted_image