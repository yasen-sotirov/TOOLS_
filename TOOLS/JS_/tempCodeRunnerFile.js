
const yearUntilRetirement = (birthYear, firstName) => {
	const age = 2024 - birthYear;
	const retirement = 65 - age;
	return `${firstName} retires in ${retirement} years.`; 
}
console.log(yearUntilRetirement(1986, 'Yasen'))
