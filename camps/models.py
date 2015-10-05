import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

from bornhack.utils import CreatedUpdatedModel, UUIDModel


class Camp(CreatedUpdatedModel, UUIDModel):
    class Meta:
        verbose_name = _('Camp')
        verbose_name_plural = _('Camps')

    name = models.CharField(
        verbose_name=_('Name'),
        help_text=_('Name of the camp, ie. Bornhack.'),
        max_length=255,
    )

    start = models.DateTimeField(
        verbose_name=_('Start date'),
        help_text=_('When the camp starts.'),
        unique=True,
    )

    end = models.DateTimeField(
        verbose_name=_('End date'),
        help_text=_('When the camp ends.'),
        unique=True,
    )

    def __str__(self):
        return _('{} {}').format(
            self.name,
            self.start.year,
        )

    def create_days(self):
        delta = self.end - self.start
        for day_offset in range(1, delta.days + 1):
            day, created = self.days.get_or_create(
                date=self.start + datetime.timedelta(days=day_offset)
            )
            if created:
                print('{} created'.format(day))

    def save(self, **kwargs):
        super().save(**kwargs)
        self.create_days()


class Day(CreatedUpdatedModel, UUIDModel):
    class Meta:
        verbose_name = _('Day')
        verbose_name_plural = _('Days')

    camp = models.ForeignKey(
        'camps.Camp',
        verbose_name=_('Camp'),
        help_text=_('Which camp does this day belong to.'),
        related_name='days',
    )

    date = models.DateField(
        verbose_name=_('Date'),
        help_text=_('What date?')
    )


class Expense(CreatedUpdatedModel, UUIDModel):
    class Meta:
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')

    camp = models.ForeignKey(
        'camps.Camp',
        verbose_name=_('Camp'),
        help_text=_('The camp to which this expense relates to.'),
    )

    description = models.CharField(
        verbose_name=_('Description'),
        help_text=_('What this expense covers.'),
        max_length=255,
    )

    amount = models.DecimalField(
        verbose_name=_('Amount'),
        help_text=_('The amount of the expense.'),
        max_digits=7,
        decimal_places=2,
    )

    CURRENCIES = [
        ('btc', 'BTC'),
        ('dkk', 'DKK'),
        ('eur', 'EUR'),
        ('sek', 'SEK'),
    ]

    currency = models.CharField(
        verbose_name=_('Currency'),
        help_text=_('What currency the amount is in.'),
        choices=CURRENCIES,
        max_length=3,
    )

    covered_by = models.ForeignKey(
        'auth.User',
        verbose_name=_('Covered by'),
        help_text=_('Which user, if any, covered this expense.'),
        null=True,
        blank=True,
    )

    def __str__(self):
        return _('{} {} for {}').format(
            self.amount,
            self.get_currency_display(),
            self.camp,
        )


class Signup(CreatedUpdatedModel, UUIDModel):
    class Meta:
        verbose_name = _('Signup')
        verbose_name_plural = _('Signups')

    camp = models.ForeignKey(
        'camps.Camp',
        verbose_name=_('Camp'),
        help_text=_('The camp that has been signed up for.'),
    )

    user = models.ForeignKey(
        'auth.User',
        verbose_name=_('User'),
        help_text=_('The user that has signed up.'),
    )

    cost = models.DecimalField(
        verbose_name=_('Cost'),
        help_text=_('What the user should/is willing to pay for this signup.'),
        max_digits=7,
        decimal_places=2,
        default=1500.0
    )

    paid = models.BooleanField(
        verbose_name=_('Paid?'),
        help_text=_('Whether the user has paid.'),
        default=False,
    )
