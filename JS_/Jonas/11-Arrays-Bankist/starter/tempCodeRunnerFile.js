const user = 'Steven Thomas Williams';

const createUsername = function (name) {
  const username = user
    .toLowerCase()
    .split(' ')
    .map(name => name[0])
    .join('');
  return username;
};

console.log(createUsername(user));
