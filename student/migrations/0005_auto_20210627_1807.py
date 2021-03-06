# Generated by Django 3.1.5 on 2021-06-27 15:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210627_1807'),
        ('student', '0004_auto_20210609_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='bank',
            field=models.CharField(blank=True, choices=[('Εθνική Τράπεζα', 'Εθνική Τράπεζα'), ('Πειραιώς', 'Πειραιώς'), ('Eurobank', 'Eurobank'), ('Alpha Bank', 'Alpha Bank')], max_length=30, verbose_name='Τράπεζα'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Ημερομηνία Δημιουργίας'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='document',
            field=models.FileField(upload_to=student.models.user_directory_path, verbose_name='Αρχείο'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='installment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.paymentinstallment', verbose_name='Δόση'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('Αποδεκτή', 'Αποδεκτή'), ('Μη Αποδεκτή', 'Μη Αποδεκτή'), ('Υπο Έλεγχο', 'Υπο Έλεγχο')], default='Υπο Έλεγχο', max_length=20, verbose_name='Κατάσταση'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student', verbose_name='Φοιτητής/ρια'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='transaction_number',
            field=models.PositiveIntegerField(blank=True, help_text='Παρακαλώ εισάγετε τον 9ψήφιο κωδικό συναλλαγής', unique=True, verbose_name='Αριθμός Συναλλαγής'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Ημερομηνία Ενημέρωσης'),
        ),
        migrations.AlterField(
            model_name='paymentinstallment',
            name='amount',
            field=models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Ποσό'),
        ),
        migrations.AlterField(
            model_name='paymentinstallment',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Ημερομηνία Προθεσμίας'),
        ),
        migrations.AlterField(
            model_name='paymentinstallment',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Όνομα'),
        ),
        migrations.AlterField(
            model_name='paymentinstallment',
            name='postgrad_year',
            field=models.IntegerField(blank=True, choices=[(2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2021, null=True, verbose_name='Έτος Προγράμματος'),
        ),
        migrations.AlterField(
            model_name='paymentinstallment',
            name='program_duration',
            field=models.CharField(choices=[('Πλήρης Φοίτηση', 'Πλήρης Φοίτηση'), ('Μερική Φοίτηση', 'Μερική Φοίτηση')], default='Πλήρης Φοίτηση', max_length=14, verbose_name='Διάρκεια Σπουδών'),
        ),
    ]
