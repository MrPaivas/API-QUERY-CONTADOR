from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ApoioMulti(db.Model):
    idapoio_multi = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    contador = db.Column(db.Integer)

    def __repr__(self):
        return 'ApoioMulti %r' % self.idapoio_multi


class Biblioteca(db.Model):
    idbiblioteca = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    contador = db.Column(db.Integer)

    def __repr__(self):
        return 'ApoioMulti %r' % self.idbiblioteca


class Clinica(db.Model):
    idclinia = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    contador = db.Column(db.Integer)

    def __repr__(self):
        return 'ApoioMulti %r' % self.idclinica


class Comercial(db.Model):
    idcomercial = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    contador = db.Column(db.Integer)

    def __repr__(self):
        return 'ApoioMulti %r' % self.idcomercial


class Cordenacao(db.Model):
    idcordenacao = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    contador = db.Column(db.Integer)

    def __repr__(self):
        return 'ApoioMulti %r' % self.idcordenacao


class Psicologia(db.Model):
    idpsicologia = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    contador = db.Column(db.Integer)

    def __repr__(self):
        return 'ApoioMulti %r' % self.idpsicologia


class SecAcad(db.Model):
    idsec_acad = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    contador = db.Column(db.Integer)

    def __repr__(self):
        return 'ApoioMulti %r' % self.idsec_acad


class Secretaria(db.Model):
    idsecretaria = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    contador = db.Column(db.Integer)

    def __repr__(self):
        return 'ApoioMulti %r' % self.idsecretaria