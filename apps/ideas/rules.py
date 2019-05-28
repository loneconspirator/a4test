import rules

from adhocracy4.modules import predicates as module_predicates

from . import models

rules.add_perm(
    'a4test_ideas.view_idea',
    module_predicates.is_allowed_view_item
)

rules.add_perm(
    'a4test_ideas.add_idea',
    module_predicates.is_allowed_add_item(models.Idea)
)

rules.add_perm(
    'a4test_ideas.change_idea',
    module_predicates.is_allowed_change_item
)

rules.add_perm(
    'a4test_ideas.rate_idea',
    module_predicates.is_allowed_rate_item
)

rules.add_perm(
    'a4test_ideas.comment_idea',
    module_predicates.is_allowed_comment_item
)

rules.add_perm(
    'a4test_ideas.moderate_idea',
    module_predicates.is_context_moderator
    | module_predicates.is_context_initiator
)

rules.add_perm(
    'a4test_ideas.export_ideas',
    module_predicates.is_context_moderator
    | module_predicates.is_context_initiator
)
