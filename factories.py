# Copyright 2016, 2022 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=too-few-public-methods

"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category


class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        """Maps factory to data model"""
        
        model = Product
        id = factory.Sequence(lambda n: n)
    
        ## Add code to create Fake Products 
        id = factory.Sequence(lambda n: n)
        name = factory.Faker("name")
        description = factory.Faker("description")
        price = factory.Faker("price")        
        category = factory.Faker("category")
        available = FuzzyChoice(choices=[True, False])


        # Generate 100 Fake products

        def test_(self):
            for _ in range(100):
                record = 
                {
                    "id": fake.id(),
                    "name": fake.name(),
                    "description": fake.description(),
                    "price": fake.price()
                    "category": fake.category()
                }
            data.append(record)
            # Create a pandas DataFrame
            df = pd.DataFrame(data)

        def update(self):
            """Updates a Account to the database"""
            logger.info("Saving %s", self.name)
            if not self.id:
                raise DataValidationError("Update called with empty ID field")
            db.session.commit()





