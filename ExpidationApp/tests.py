from types import SimpleNamespace

from django.contrib.auth.models import AnonymousUser
from django.template.loader import get_template
from django.test import TestCase
from django.urls import reverse


class ExpeditionListActionsTests(TestCase):
    def setUp(self):
        self.expedition = SimpleNamespace(
            pk=1,
            reference="EXP_2600001",
            ville_depart="Tunis",
            ville_arrivee="Sfax",
            poids_kg=10,
            get_status_display=lambda: "publiee",
        )

    def render_list(self, user):
        return get_template("expidation/list.html").render({
            "list": [self.expedition],
            "user": user,
        })

    def test_anonymous_user_does_not_see_expedition_actions(self):
        content = self.render_list(AnonymousUser())

        self.assertNotIn("Actions", content)
        self.assertNotIn("Modifier", content)
        self.assertNotIn("Supprimer", content)

    def test_authenticated_user_sees_expedition_actions(self):
        user = SimpleNamespace(is_authenticated=True, username="testuser")

        content = self.render_list(user)

        self.assertIn("Modifier", content)
        self.assertIn("Supprimer", content)
        self.assertIn(reverse("Expidation:deleteview", args=[self.expedition.pk]), content)

    def test_anonymous_user_is_redirected_from_delete_views(self):
        response = self.client.get(
            reverse("Expidation:deleteview", args=[self.expedition.pk])
        )
        self.assertEqual(response.status_code, 302)

        response = self.client.get(
            reverse("Expidation:delete", args=[self.expedition.reference])
        )
        self.assertEqual(response.status_code, 302)
