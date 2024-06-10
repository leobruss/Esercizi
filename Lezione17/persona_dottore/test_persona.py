import unittest
from Esercizi.Lezione17.persona_dottore.persona import Persona
from Esercizi.Lezione17.persona_dottore.dottore import Dottore
from Esercizi.Lezione17.persona_dottore.paziente import Paziente
from Esercizi.Lezione17.persona_dottore.fatture import Fattura

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
    def setUp(self):
        self.doctor = Dottore("Giovanni", "Bianchi", "Pediatra", 150.0)
        self.doctor.setAge(40)
        self.patients = [Paziente("Luca", "Verdi", "ID12345"), Paziente("Anna", "Neri", "ID67890")]
        self.fattura = Fattura(self.patients, self.doctor)

    def test_initialization(self):
        self.assertEqual(self.fattura.getFatture(), 2)
        self.assertEqual(self.fattura.getSalary(), 300.0)

    def test_add_patient(self):
        new_patient = Paziente("Mario", "Rossi", "ID11223")
        self.fattura.addPatient(new_patient)
        self.assertEqual(self.fattura.getFatture(), 3)
        self.assertEqual(self.fattura.getSalary(), 450.0)

    def test_remove_patient(self):
        self.fattura.removePatient("ID12345")
        self.assertEqual(self.fattura.getFatture(), 2)
        self.assertEqual(self.fattura.getSalary(), 300.0)




if __name__ == '__main__':
    unittest.main()
        
