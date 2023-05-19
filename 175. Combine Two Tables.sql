select firstName, lastName, city, state from Person left join Address ON person.personId = Address.personId;
