// Konvert celsius to Kelvins

const measureKelvin = function () {
  const measurment = {
    type: "temp",
    units: "celsius",
    value: prompt("Type degree in celsius: "),
  };

  const kelvin = Number(measurment.value) + 273;
  return kelvin;
};

console.log(measureKelvin());
