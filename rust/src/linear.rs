use std::fmt;

pub struct LinearVector {
	dimension: usize,
	coordinates: Vec<i32>
}

impl fmt::Display for LinearVector {
	fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
		write!(f, "Vector: [{:?}]", self.coordinates)
	}
}

impl LinearVector {
	pub fn new(coordinates_in:Vec<i32>) -> LinearVector {
		LinearVector {dimension:coordinates_in.len(), coordinates: coordinates_in}
	}
}
