/**
 * 2007-2022 ETS-Soft
 *
 * NOTICE OF LICENSE
 *
 * This file is not open source! Each license that you purchased is only available for 1 wesite only.
 * If you want to use this file on more websites (or projects), you need to purchase additional licenses. 
 * You are not allowed to redistribute, resell, lease, license, sub-license or offer our resources to any third party.
 * 
 * DISCLAIMER
 *
 * Do not edit or add to this file if you wish to upgrade PrestaShop to newer
 * versions in the future. If you wish to customize PrestaShop for your
 * needs please contact us for extra customization service at an affordable price
 *
 *  @author ETS-Soft <etssoft.jsc@gmail.com>
 *  @copyright  2007-2022 ETS-Soft
 *  @license    Valid for 1 website (or project) for each purchase of license
 *  International Registered Trademark & Property of ETS-Soft
 */

$(document).ready(function(){ 
    if($('.new_products_list_wrapper.layout-slide:not(.slick-slider):not(.product_list_16)').length >0)
    {
        $('.new_products_list_wrapper.layout-slide:not(.slick-slider):not(.product_list_16)').each(function(){
            var this_slick = $(this);
            var count_products = this_slick.find('.product-miniature').length;
            $(this).slick({
                  slidesToShow: count_products && count_products <  ets_newp_nbItemsPerLine ? count_products :ets_newp_nbItemsPerLine,
                  slidesToScroll: 1,
                  arrows: true,
                  autoplay:this_slick.hasClass('auto'),
                  responsive: [
                      {
                          breakpoint: 1199,
                          settings: {
                              slidesToShow: count_products && count_products <  ets_newp_nbItemsPerLine ? count_products :ets_newp_nbItemsPerLine
                          }
                      },
                      {
                          breakpoint: 992,
                          settings: {
                              slidesToShow: count_products && count_products <  ets_newp_nbItemsPerLineTablet ? count_products :ets_newp_nbItemsPerLineTablet
                          }
                      },
                      {
                          breakpoint: 768,
                          settings: {
                              slidesToShow: count_products && count_products <  ets_newp_nbItemsPerLineMobile ? count_products :ets_newp_nbItemsPerLineMobile
                          }
                      },
                      {
                          breakpoint: 480,
                          settings: {
                            slidesToShow: count_products && count_products <  ets_newp_nbItemsPerLineMobile ? count_products :ets_newp_nbItemsPerLineMobile
                          }
                      }
                   ]
            });
        });
   }
});