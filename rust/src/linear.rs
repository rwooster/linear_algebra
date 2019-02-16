use std::fmt;
use std::ops::{Add, Sub};

#[derive(Debug)]
pub struct LinearVector {
	dimension: usize,
	coordinates: Vec<i32>
}

impl fmt::Display for LinearVector {
	fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
		write!(f, "Vector: [{:?}]", self.coordinates)
	}
}

impl PartialEq for LinearVector {
    fn eq(&self, other: &Self) -> bool {
        self.coordinates == other.coordinates
    }
}

impl Add for LinearVector {
    type Output = LinearVector;

    fn add(self, other: Self) -> LinearVector {
        LinearVector::new(self.coordinates.iter().zip(&other.coordinates).map(|(a, b)| a+b).collect())
    }
}

impl Sub for LinearVector {
    type Output = LinearVector;

    fn sub(self, other: Self) -> LinearVector {
        LinearVector::new(self.coordinates.iter().zip(&other.coordinates).map(|(a, b)| a-b).collect())
    }
}

impl LinearVector {
	pub fn new(coordinates_in:Vec<i32>) -> LinearVector {
		LinearVector {dimension:coordinates_in.len(), coordinates: coordinates_in}
	}

    pub fn scalar_multiply(&self, scalar: i32) -> LinearVector {
        LinearVector::new(self.coordinates.iter().map(|a| a*scalar).collect())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_equality() {
        let vector1 = LinearVector::new(vec!(1, 2, 3));
        let vector2 = LinearVector::new(vec!(1, 2, 3));
        assert!(vector1 == vector2);

        let vector3 = LinearVector::new(vec!(1, 2, 4));
        assert!(vector1 != vector3);

        let vector4 = LinearVector::new(vec!(1, 2, 3, 5));
        assert!(vector1 != vector4);
    }

    #[test]
    fn test_addition() {
        let vector1 = LinearVector::new(vec!(1, 2, 3));
        let vector2 = LinearVector::new(vec!(1, 2, 3));
        let expected_sum = LinearVector::new(vec!(2, 4, 6));

        assert!(vector1 + vector2 == expected_sum);
    }

    #[test]
    fn test_subtraction() {
        let vector1 = LinearVector::new(vec!(4, 4, 3));
        let vector2 = LinearVector::new(vec!(1, 2, 3));
        let expected_difference = LinearVector::new(vec!(3, 2, 0));

        assert!(vector1 - vector2 == expected_difference);
    }

    #[test]
    fn test_scalar_multiply() {
        let vector = LinearVector::new(vec!(1, 2, 3, 4));
        let doubled = vector.scalar_multiply(2);
        let expected = LinearVector::new(vec!(2, 4, 6, 8));

        assert!(doubled == expected);
    }
}


