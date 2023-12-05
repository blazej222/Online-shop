<?php
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
 * @author ETS-Soft <etssoft.jsc@gmail.com>
 * @copyright  2007-2022 ETS-Soft
 * @license    Valid for 1 website (or project) for each purchase of license
 *  International Registered Trademark & Property of ETS-Soft
 */

if (!defined('_PS_VERSION_'))
    exit;

class Ets_newproducts_defines
{
    public static $instance;
    public function __construct()
    {
        $this->context = Context::getContext();
        if (is_object($this->context->smarty)) {
            $this->smarty = $this->context->smarty;
        }
    }
    public static function getInstance()
    {
        if (!(isset(self::$instance)) || !self::$instance) {
            self::$instance = new Ets_newproducts_defines();
        }
        return self::$instance;
    }
    public function l($string)
    {
        return Translate::getModuleTranslation('ets_newproducts', $string, pathinfo(__FILE__, PATHINFO_FILENAME));
    }
    public function getConfigInputs()
    {
        return array(
            array(
                'name' => 'ETS_NEWP_TILE_HOME_BLOCK',
                'label' => $this->l('Title'),
                'lang'=>true,
                'type'=>'text',
                'form_group_class'=> 'position home_block',
                'validate'=>'isCleanHtml',
                'default' => $this->l('New products'),
                'default_lang' => 'New products',
                'showRequired' => true,
            ),
            array(
                'type'=> 'text',
                'name' => 'ETS_NEWP_NUMBER_PRODUCT_IN_HOME',
                'label' => $this->l('Number of products to display'),
                'form_group_class'=> 'position home_block',
                'validate' => 'isUnsignedInt',
                'default' => 8,
                'desc' => $this->l('Leave blank to show all new products'),
            ),
            array(
                'type' => 'radio',
                'name' => 'ETS_NEWP_DISPLAY_TYPE_IN_HOME',
                'label' => $this->l('Display type'),
                'form_group_class'=> 'position home_block',
                'validate' => 'isCleanHtml',
                'default' => 'slide',
                'values' => array(
                    array(
                        'id'=> 'ETS_NEWP_DISPLAY_TYPE_IN_HOME_gird',
                        'label' => $this->l('Grid'),
                        'value'=>'gird',
                    ),
                    array(
                        'id'=> 'ETS_NEWP_DISPLAY_TYPE_IN_HOME_slide',
                        'label' => $this->l('Slider'),
                        'value'=>'slide',
                    ),
                ),
            ),
            array(
                'type' => 'switch',
                'name' => 'ETS_NEWP_AUTO_PLAY_HOME',
                'label' => $this->l('Auto-play slider'),
                'default' => 1,
                'validate' => 'isInt',
                'values' => array(
                    array(
                        'label' => $this->l('Yes'),
                        'id' => 'ETS_NEWP_AUTO_PLAY_HOME_on',
                        'value' => 1,
                    ),
                    array(
                        'label' => $this->l('No'),
                        'id' => 'ETS_NEWP_AUTO_PLAY_HOME_off',
                        'value' => 0,
                    )
                ),
                'form_group_class'=> 'position home_block',
            ),
            array(
                'name' => 'ETS_NEWP_TILE_LEFT_BLOCK',
                'label' => $this->l('Title'),
                'lang'=>true,
                'type'=>'text',
                'form_group_class'=> 'position left_block',
                'validate'=>'isCleanHtml',
                'default' => $this->l('New products'),
                'default_lang' => 'New products',
                'showRequired' => true,
            ),
            array(
                'type'=> 'text',
                'name' => 'ETS_NEWP_NUMBER_PRODUCT_IN_LEFT',
                'label' => $this->l('Number of products to display'),
                'form_group_class'=> 'position left_block',
                'validate' => 'isUnsignedInt',
                'default' =>8,
                'desc' => $this->l('Leave blank to show all new products'),
            ),
            array(
                'type' => 'radio',
                'name' => 'ETS_NEWP_DISPLAY_TYPE_IN_LEFT',
                'label' => $this->l('Display type'),
                'form_group_class'=> 'position left_block',
                'validate' => 'isCleanHtml',
                'default' => 'slide',
                'values' => array(
                    array(
                        'id'=> 'ETS_NEWP_DISPLAY_TYPE_IN_LEFT_gird',
                        'label' => $this->l('Grid'),
                        'value'=>'gird',
                    ),
                    array(
                        'id'=> 'ETS_NEWP_DISPLAY_TYPE_IN_LEFT_slide',
                        'label' => $this->l('Slider'),
                        'value'=>'slide',
                    ),
                ),
                
            ),
            array(
                'type' => 'switch',
                'name' => 'ETS_NEWP_AUTO_PLAY_LEFT',
                'label' => $this->l('Auto-play slider'),
                'default' => 1,
                'validate' => 'isInt',
                'values' => array(
                    array(
                        'label' => $this->l('Yes'),
                        'id' => 'ETS_NEWP_AUTO_PLAY_LEFT_on',
                        'value' => 1,
                    ),
                    array(
                        'label' => $this->l('No'),
                        'id' => 'ETS_NEWP_AUTO_PLAY_LEFT_off',
                        'value' => 0,
                    )
                ),
                'form_group_class'=> 'position left_block',
            ),
            array(
                'name' => 'ETS_NEWP_TILE_RIGHT_BLOCK',
                'label' => $this->l('Title'),
                'lang'=>true,
                'type'=>'text',
                'form_group_class'=> 'position right_block',
                'validate'=>'isCleanHtml',
                'default' => $this->l('New products'),
                'default_lang' => 'New products',
                'showRequired' => true,
            ),
            array(
                'type'=> 'text',
                'name' => 'ETS_NEWP_NUMBER_PRODUCT_IN_RIGHT',
                'label' => $this->l('Number of products to display'),
                'form_group_class'=> 'position right_block',
                'validate' => 'isUnsignedInt',
                'default' => 8,
                'desc' => $this->l('Leave blank to show all new products'),
            ),
            array(
                'type' => 'radio',
                'name' => 'ETS_NEWP_DISPLAY_TYPE_IN_RIGHT',
                'label' => $this->l('Display type'),
                'form_group_class'=> 'position right_block',
                'validate' => 'isCleanHtml',
                'default' => 'slide',
                'values' => array(
                    array(
                        'id'=> 'ETS_NEWP_DISPLAY_TYPE_IN_RIGHT_gird',
                        'label' => $this->l('Grid'),
                        'value'=>'gird',
                    ),
                    array(
                        'id'=> 'ETS_NEWP_DISPLAY_TYPE_IN_RIGHT_slide',
                        'label' => $this->l('Slider'),
                        'value'=>'slide',
                    ),
                ),
            ),
            array(
                'type' => 'switch',
                'name' => 'ETS_NEWP_AUTO_PLAY_RIGHT',
                'label' => $this->l('Auto-play slider'),
                'default' => 1,
                'validate' => 'isInt',
                'values' => array(
                    array(
                        'label' => $this->l('Yes'),
                        'id' => 'ETS_NEWP_AUTO_PLAY_RIGHT_on',
                        'value' => 1,
                    ),
                    array(
                        'label' => $this->l('No'),
                        'id' => 'ETS_NEWP_AUTO_PLAY_RIGHT_off',
                        'value' => 0,
                    )
                ),
                'form_group_class'=> 'position right_block',
            ),
            array(
                'name' => 'ETS_NEWP_TILE_PRODUCT_BLOCK',
                'label' => $this->l('Title'),
                'lang'=>true,
                'type'=>'text',
                'form_group_class'=> 'position product_block',
                'validate'=>'isCleanHtml',
                'default' => $this->l('New products'),
                'default_lang' => 'New products',
                'showRequired' => true,
            ),
            array(
                'type'=> 'text',
                'name' => 'ETS_NEWP_NUMBER_PRODUCT_IN_PRODUCT',
                'label' => $this->l('Number of products to display'),
                'form_group_class'=> 'position product_block',
                'validate' => 'isUnsignedInt',
                'default' => 8,
                'desc' => $this->l('Leave blank to show all new products'),
            ),
            array(
                'type' => 'radio',
                'name' => 'ETS_NEWP_DISPLAY_TYPE_IN_PRODUCT',
                'label' => $this->l('Display type'),
                'form_group_class'=> 'position product_block',
                'validate' => 'isCleanHtml',
                'default' => 'slide',
                'values' => array(
                    array(
                        'id'=> 'ETS_NEWP_DISPLAY_TYPE_IN_PRODUCT_gird',
                        'label' => $this->l('Grid'),
                        'value'=>'gird',
                    ),
                    array(
                        'id'=> 'ETS_NEWP_DISPLAY_TYPE_IN_PRODUCT_slide',
                        'label' => $this->l('Slider'),
                        'value'=>'slide',
                    ),
                ),
            ),
            array(
                'type' => 'switch',
                'name' => 'ETS_NEWP_AUTO_PLAY_PRODUCT',
                'label' => $this->l('Auto-play slider'),
                'default' => 1,
                'validate' => 'isInt',
                'values' => array(
                    array(
                        'label' => $this->l('Yes'),
                        'id' => 'ETS_NEWP_AUTO_PLAY_PRODUCT_on',
                        'value' => 1,
                    ),
                    array(
                        'label' => $this->l('No'),
                        'id' => 'ETS_NEWP_AUTO_PLAY_PRODUCT_off',
                        'value' => 0,
                    )
                ),
                'form_group_class'=> 'position product_block',
            ),
        );
    }
    public static function getNewProducts($id_lang, $page_number = 0, $nb_products = 10, $count = false, $order_by = null, $order_way = null, Context $context = null)
    {
        $now = date('Y-m-d') . ' 00:00:00';
        if (!$context) {
            $context = Context::getContext();
        }

        $front = true;
        if (!in_array($context->controller->controller_type, ['front', 'modulefront'])) {
            $front = false;
        }

        if ($page_number < 1) {
            $page_number = 1;
        }
        if (empty($order_by) || $order_by == 'position') {
            $order_by = 'date_add';
        }
        if (empty($order_way)) {
            $order_way = 'DESC';
        }
        if ($order_by == 'id_product' || $order_by == 'price' || $order_by == 'date_add' || $order_by == 'date_upd') {
            $order_by_prefix = 'product_shop';
        } elseif ($order_by == 'name') {
            $order_by_prefix = 'pl';
        }
        if (!Validate::isOrderBy($order_by) || !Validate::isOrderWay($order_way)) {
            die(Tools::displayError());
        }

        $sql_groups = '';
        if (Group::isFeatureActive()) {
            $groups = FrontController::getCurrentCustomerGroups();
            $sql_groups = ' AND EXISTS(SELECT 1 FROM `' . _DB_PREFIX_ . 'category_product` cp
            JOIN `' . _DB_PREFIX_ . 'category_group` cg ON (cp.id_category = cg.id_category AND cg.`id_group` ' . (count($groups) ? 'IN (' . implode(',', $groups) . ')' : '=' . (int) Group::getCurrent()->id) . ')
            WHERE cp.`id_product` = p.`id_product`)';
        }

        if (strpos($order_by, '.') > 0) {
            $order_by = explode('.', $order_by);
            $order_by_prefix = $order_by[0];
            $order_by = $order_by[1];
        }

        $nb_days_new_product = (int) Configuration::get('PS_NB_DAYS_NEW_PRODUCT');

        if ($count) {
            $sql = 'SELECT COUNT(p.`id_product`) AS nb
                    FROM `' . _DB_PREFIX_ . 'product` p
                    ' . Shop::addSqlAssociation('product', 'p') . '
                    WHERE product_shop.`active` = 1
                    AND product_shop.`date_add` > "' . date('Y-m-d', strtotime('-' . $nb_days_new_product . ' DAY')) . '"
                    ' . ($front ? ' AND product_shop.`visibility` IN ("both", "catalog")' : '') . '
                    ' . $sql_groups;

            return (int) Db::getInstance(_PS_USE_SQL_SLAVE_)->getValue($sql);
        }
        $sql = new DbQuery();
        $sql->select(
            'p.*, product_shop.*, stock.out_of_stock, IFNULL(stock.quantity, 0) as quantity, pl.`description`, pl.`description_short`, pl.`link_rewrite`, pl.`meta_description`,
            pl.`meta_keywords`, pl.`meta_title`, pl.`name`, pl.`available_now`, pl.`available_later`, image_shop.`id_image` id_image, il.`legend`, m.`name` AS manufacturer_name,
            (DATEDIFF(product_shop.`date_add`,
                DATE_SUB(
                    "' . $now . '",
                    INTERVAL ' . $nb_days_new_product . ' DAY
                )
            ) > 0) as new'
        );

        $sql->from('product', 'p');
        $sql->join(Shop::addSqlAssociation('product', 'p'));
        $sql->leftJoin(
            'product_lang',
            'pl',
            '
            p.`id_product` = pl.`id_product`
            AND pl.`id_lang` = ' . (int) $id_lang . Shop::addSqlRestrictionOnLang('pl')
        );
        $sql->leftJoin('image_shop', 'image_shop', 'image_shop.`id_product` = p.`id_product` AND image_shop.cover=1 AND image_shop.id_shop=' . (int) $context->shop->id);
        $sql->leftJoin('image_lang', 'il', 'image_shop.`id_image` = il.`id_image` AND il.`id_lang` = ' . (int) $id_lang);
        $sql->leftJoin('manufacturer', 'm', 'm.`id_manufacturer` = p.`id_manufacturer`');

        $sql->where('product_shop.`active` = 1');
        if ($front) {
            $sql->where('product_shop.`visibility` IN ("both", "catalog")');
        }
        $sql->where('product_shop.`date_add` > "' . date('Y-m-d', strtotime('-' . $nb_days_new_product . ' DAY')) . '"');
        if (Group::isFeatureActive()) {
            $groups = FrontController::getCurrentCustomerGroups();
            $sql->where('EXISTS(SELECT 1 FROM `' . _DB_PREFIX_ . 'category_product` cp
            JOIN `' . _DB_PREFIX_ . 'category_group` cg ON (cp.id_category = cg.id_category AND cg.`id_group` ' . (count($groups) ? 'IN (' . implode(',', $groups) . ')' : '=' . (int) Group::getCurrent()->id) . ')
            WHERE cp.`id_product` = p.`id_product`)');
        }

        if ($order_by !== 'price') {
            $sql->orderBy((isset($order_by_prefix) ? pSQL($order_by_prefix) . '.' : '') . '`' . pSQL($order_by) . '` ' . pSQL($order_way));
            if($nb_products && $nb_products!==true)
            {
                $sql->limit($nb_products, (int) (($page_number - 1) * $nb_products));
            }
        }

        if (Combination::isFeatureActive()) {
            $sql->select('product_attribute_shop.minimal_quantity AS product_attribute_minimal_quantity, IFNULL(product_attribute_shop.id_product_attribute,0) id_product_attribute');
            $sql->leftJoin('product_attribute_shop', 'product_attribute_shop', 'p.`id_product` = product_attribute_shop.`id_product` AND product_attribute_shop.`default_on` = 1 AND product_attribute_shop.id_shop=' . (int) $context->shop->id);
        }
        $sql->join(Product::sqlStock('p', 0));

        $result = Db::getInstance(_PS_USE_SQL_SLAVE_)->executeS($sql);

        if (!$result) {
            return false;
        }

        if ($order_by === 'price') {
            Tools::orderbyPrice($result, $order_way);
            $result = array_slice($result, (int) (($nb_products - 1) * $page_number), (int) $page_number);
        }
        $products_ids = [];
        foreach ($result as $row) {
            $products_ids[] = $row['id_product'];
        }
        // Thus you can avoid one query per product, because there will be only one query for all the products of the cart
        Product::cacheFrontFeatures($products_ids, $id_lang);

        return Product::getProductsProperties((int) $id_lang, $result);
    }
}