#!/usr/bin/node

exports.esrever = function (list) {
  const reversed_list = [];
  for (let i = 0; i <= list.length - 1; i++) {
    reversed_list.unshift(list[i]);
  }
  return reversed_list;
};
