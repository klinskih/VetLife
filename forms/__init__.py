from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from VetLife import db
BaseModelForm = model_form_factory(FlaskForm)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

from .Login import LoginForm
from .Medicine import MedicineForm
from .Dosage import DosageForm
from .Unit import UnitForm
from .Profile import ProfileForm
from .ActiveSubstance import ActiveSubstanceForm
from .SearchForm import SearchForm
from .CureSchema import CureSchemaForm
from .CalcDosage import CalcDosageForm
