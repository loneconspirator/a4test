import rules
from rules.predicates import is_superuser

from .predicates import is_initiator

rules.add_perm(
    'a4test_organisations.change_organisation',
    is_superuser | is_initiator
)
