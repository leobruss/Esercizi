import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fatture import Fattura

class TestPersona(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Persona('Mario', 'Rossi')
    
    def test_initialization(self):
        self.assertEqual(self.person.getName(), 'Mario')
        self.assertEqual(self.person.getLastname(), 'Rossi')
    
    def test_set_name(self):
        self.person.setName('Mario')
        self.assertEqual(self.person.getName(), 'Mario')

    def test_set_last_name(self):
        self.person.setLastName('Rossi')
        self.assertEqual(self.person.getLastname(), 'Rossi')

    def test_set_age(self):
        self.person.setAge(30)
        self.assertEqual(self.person.getAge(), 30)

class TestDottore (unittest.TestCase):
    def setUp(self) -> None:
        self.dottore: Dottore = Dottore('Mario', 'Rossi', "Ostetrico", 150.0)

    def test_initialization(self):
       self.assertEqual(self.dottore.getName(), 'Mario')
       self.assertEqual(self.dottore.getLastname(), 'Rossi')
       self.assertEqual(self.dottore.getSpecialization(), 'Ostetrico')
       self.assertEqual(self.dottore.getParcel(), 150.0)

    def test_is_valid_doctor(self):
       self.dottore.setAge(25)
       self.assertFalse(self.dottore.isAValidDoctor())
       self.dottore.setAge(30)
       self.assertFalse(self.dottore.isAValidDoctor())
       self.dottore.setAge(70)
       self.assertTrue(self.dottore.isAValidDoctor())
    
class TestPaziente(unittest.TestCase):

    def setUp(self):
        self.paziente = Paziente('Framcesco', 'Bartolomei', '1234567890')

    def test_initialization(self):
        self.assertEqual(self.paziente.getName(), 'Framcesco')
        self.assertEqual(self.paziente.getLastname(), 'Bartolomei')
        self.assertEqual(self.paziente.getidCode(), '1234567890')
    
class TestFattura(unittest.TestCase):
    paziente1 = Paziente("Leonardo", "Brussani", "LB24004")
    paziente2 = Paziente("Matteo", "Cardelli", "MC24004")
    paziente3 = Paziente("Lorenzo", "Brussani", "LB09097")

    def setUp(self):
        self.dottore = Dottore('Mario', 'Rossi', 'Ostetrico', 150.0)
        self.dottore.setAge(45)
        self.fattura = Fattura([(self.paziente1, self.paziente2, self.paziente3)], self.dottore)

    def test_initialization(self):
        self.assertEqual(self.fattura.getFatture(), 2)
        self.assertEqual(self.fattura.getSalary(), 450)

    def test_add_remove_paziente(self):

        self.fattura.addPatient(self.paziente1)
        self.assertEqual(len(self.fattura._patient), 1)
        self.assertIn(self.paziente1, self.fattura._patient)

        self.fattura.addPatient(self.paziente2)
        self.assertEqual(len(self.fattura._patient), 2)
        self.assertIn(self.paziente2, self.fattura._patient)

        self.fattura.removePatient(self.paziente1)
        self.assertEqual(len(self.fattura._patient), 1)
        self.assertNotIn(self.paziente1, self.fattura._patient)

        self.fattura.removePatient(self.paziente2)
        self.assertEqual(len(self.fattura._patient), 0)
        self.assertNotIn(self.paziente2, self.fattura._patient)

    def test_salary_calculation(self):
        self.fattura.addPatient(Paziente('Carlo', 'Verdi', '0987654321'))
        self.fattura.addPatient(Paziente('Giovanni', 'Neri', '5678901234'))
        self.assertEqual(self.fattura.getSalary(), 300.0)
        self.assertEqual(self.fattura.getFatture, 2)




if __name__ == '__main__':
    unittest.main()
        
