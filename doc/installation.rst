Installing and Basic Usage of XrayDB
=====================================

The X-ray database is held in the SQLite3 file ``xraydb.sqlite``.   For use
with SQLite, this file is all you need, as with::

   system~> sqlite3 xraydb.sqlite
   sqlite> .headers on
   sqlite> select * from elements where atomic_number=47;
   atomic_number|element|molar_mass|density
   47|Ag|107.868|10.48


Of course, the expectation is that you'd want to use this database within a
programming environment.   Currently, wrappers exist only for Python.


Database Schema
-------------------


The schema for the SQLite3 database is::

    CREATE TABLE Chantler (id integer primary key,
            element text, sigma_mu real, mue_f2 real, density real,
            corr_henke float, corr_cl35 float, corr_nucl float,
            energy text, f1 text, f2 text, mu_photo text,
            mu_incoh text, mu_total text);
    CREATE TABLE Coster_Kronig (id integer primary key, element text,
            initial_level text, final_level text,
            transition_probability real, total_transition_probability real);
    CREATE TABLE KeskiRahkonen_Krause (id integer primary key,
            atomic_number integer, element text, edge text, width float);
    CREATE TABLE Waasmaier (id integer primary key,
            atomic_number integer, element text, ion text,
            offset real, scale text, exponents text);
    CREATE TABLE elements (atomic_number integer primary key,
            element text, molar_mass real, density real);
    CREATE TABLE photoabsorption (id integer primary key, element text,
            log_energy text, log_photoabsorption text,
            log_photoabsorption_spline text);
    CREATE TABLE scattering (id integer primary key, element text,
            log_energy text,
            log_coherent_scatter text, log_coherent_scatter_spline text,
            log_incoherent_scatter text, log_incoherent_scatter_spline text);
    CREATE TABLE xray_levels (id integer primary key, element text,
            iupac_symbol text, absorption_edge real, fluorescence_yield real,
            jump_ratio real);
    CREATE TABLE xray_transitions (id integer primary key, element text,
            iupac_symbol text, siegbahn_symbol text, initial_level text,
            final_level text, emission_energy real, intensity real);
