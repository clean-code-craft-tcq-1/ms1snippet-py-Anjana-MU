import unittest
import sensor_validate

class SensorValidatorTest(unittest.TestCase):
  def test_reports_error_when_soc_jumps(self):
    self.assertTrue(sensor_validate.validate_soc_reading([]))
    self.assertFalse(sensor_validate.validate_soc_reading([0.0, 0.01, 0.5, 0.51]))
  
  def test_reports_error_when_current_jumps(self):
    self.assertTrue(sensor_validate.validate_current_reading([0.0,0.01]))
    self.assertTrue(sensor_validate.validate_current_reading([]))
    self.assertFalse(sensor_validate.validate_current_reading(None))
    self.assertFalse(sensor_validate.validate_current_reading([0.03, 0.03, 0.03, 0.33]))

if __name__ == "__main__":
  unittest.main()
