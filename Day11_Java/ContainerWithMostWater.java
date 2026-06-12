package Day10_placement;

	public class ContainerWithMostWater {

	    public static void main(String[] args) {

	        int[] height = {8, 8, 6, 2, 5, 8, 4, 3, 7};

	        int left = 0;
	        int right = height.length - 1;

	        int maxArea = 0;

	        while (left < right) {

	            int width = right - left;

	            int area = Math.min(height[left], height[right]) * width;

	            maxArea = Math.max(maxArea, area);

	            if (height[left] < height[right]) {
	                left++;
	            } else {
	                right--;
	            }
	        }

	        System.out.println("Maximum Area = " + maxArea);
	    }
	}


