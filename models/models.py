# -*- coding: utf-8 -*-

from openerp import models, fields, api

class videoclub_film_category(models.Model):
    """Films Categories"""
    _name = 'videoclub_film_category'
    name = fields.Char('Category',size=150, help='Name of the category')
    description = fields.Text('Description',size=200, help='Description of the category')
    parent_id = fields.Many2one('videoclub_film_category','Parent Category', help='Name of the parent category')


class videoclub_director(models.Model):
    """Directors"""
    _name = 'videoclub_director'
    name = fields.Char('Director name', size=150, help='Name of the director')
    surname1 = fields.Char('First director surname', size=150, help='First surname of the director')
    surname2 = fields.Char('Second director surname', size=150, help='Second surname of the director')
    address = fields.Char('Address', size=150, help='Director address')
    age = fields.Integer('Director age', help='Age of the director')


class videoclub_film(models.Model):
    """Films by videoclub"""
    _name = 'videoclub_film'
    name = fields.Char('Name of the film',size=150, help='Name of the film')
    category_id = fields.Many2one('videoclub_film_category','Category', help='Category of the film')
    directors = fields.Many2many('videoclub_director', 'videoclub_director_film_rel', 'film_id', 'director_id', 'Directors', help='Directors who produced the film')
    description = fields.Text('Description', help='Description of the film')
    hours = fields.Float('Film hours long', help='Hours of the film')
    product_id = fields.Many2one('product.product','Product', help='Product related to the film')
    client_id = fields.Many2one('res.partner','Client', help='Client who rents the film')
    state = fields.Selection([('rented','Rented'),('free','Free'),('notAvailable','Not available')],'State of the film', help='State of the film',default = 'free')
    type = fields.Selection([('allPublic','Film for all public'),('more13age','Film appropriate for age over 13'),('more18age','Film appropriate for age over 18')],'Type of film', help='Type of film',default = 'allPublic' )
    reserved = fields.Boolean('Reserved', help='Film reserved',default = False)
    reservation_date = fields.Date('Reserved date', help='Date when the film has been reserved')



